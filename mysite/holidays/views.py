from django.shortcuts import render, redirect
from .models import HolidayImage
from django.http import HttpResponse
# from django.contrib.auth.decorators import login_required
# import os, shutil
from . import forms
# from __future__ import print_function
import argparse
import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
from torchvision import datasets, transforms
import numpy as np
import torchvision
import torchvision.transforms as transforms

# Create your views here.
def new_image(request):
    # folder = 'media/holidays'
    # for the_file in os.listdir(folder):
    #     file_path = os.path.join(folder, the_file)
    #     try:
    #         if os.path.isfile(file_path):
    #             os.unlink(file_path)
    #         #elif os.path.isdir(file_path): shutil.rmtree(file_path)
    #     except Exception as e:
    #         print(e)
    HolidayImage.objects.all().delete()
    if request.method == 'POST':
        form = forms.HolidayImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('holidays:process')
    else:
        form = forms.HolidayImageForm
    return render(request, 'holidays/image_enter.html', {'form':form})

def image_process(request):
    images = HolidayImage.objects.all()
    def GetPlace(image_path):
        monuments = {0:'Burkingham Palace', 1:'Burj Khalifa',2:'Disney World',3:'Eiffel Tower',4:'Golden Gate Bridge',5:'Great Wall of China',6:'Pyramids',7:'Statue of Liberty',8:'Sydney Opera House',9:'Taj Mahal'}
        device = torch.device('cuda:0' if torch.cuda.is_available() else 'cpu')
        data_transform = transforms.Compose([
                transforms.RandomSizedCrop(64),
                transforms.RandomHorizontalFlip(),
                transforms.Grayscale(num_output_channels=1),
                transforms.ToTensor(),
                transforms.Normalize(mean=[0.485, 0.456, 0.406],
                                    std=[0.229, 0.224, 0.225])
            ])
        class ConvNet(nn.Module):
            def __init__(self, num_classes=10):
                super(ConvNet, self).__init__()
                self.layer1 = nn.Sequential(
                    nn.Conv2d(1, 16, kernel_size=5, stride=1, padding=2),
                    nn.BatchNorm2d(16),
                    nn.ReLU(),
                    nn.MaxPool2d(kernel_size=2, stride=2))
                self.layer2 = nn.Sequential(
                    nn.Conv2d(16, 32, kernel_size=5, stride=1, padding=2),
                    nn.BatchNorm2d(32),
                    nn.ReLU(),
                    nn.MaxPool2d(kernel_size=2, stride=2))
                self.fc = nn.Linear(8192, num_classes)

            def forward(self, x):
                #print(x.shape)
                out = self.layer1(x)
                out = self.layer2(out)
                out = out.reshape(out.size(0), -1)
                out = self.fc(out)
                return out
        model = ConvNet(10)
        model.load_state_dict(torch.load('holidays/model_weights'))
        a=0
        b=0
        c=0
        d=0
        ans=[]
        for ite in range(20):
            #print(ite)
            test_data = datasets.ImageFolder(root=image_path,
                                                    transform=data_transform)
            test_loader = torch.utils.data.DataLoader(test_data,
                                                        batch_size=32, shuffle=True,
                                                        num_workers=4)
            model.eval()  # eval mode (batchnorm uses moving mean/variance instead of mini-batch mean/variance)
            with torch.no_grad():
                correct = 0
                total = 0
                for images, labels in test_loader:
                    images = images.to(device)
                    labels = labels.to(device)
                    outputs = model(images)
                    _, predicted = torch.max(outputs.data, 1)
                    total += labels.size(0)
                    correct += (predicted == labels).sum().item()
                    #print(predicted)
                    ans.append(predicted[0].item())
        cl= max(ans,key=ans.count)
        # return monuments[cl]

    GetPlace('media')
    # return render(request, 'holidays/process_image.html', {'images':images})
    return HttpResponse(monuments[cl])