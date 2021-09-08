from os import stat
from django.shortcuts import render

from rest_framework import status
from rest_framework import response
from rest_framework import permissions
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from prediction.apps import PredictionConfig

import pandas as pd
import numpy as np
import torch
from torch.autograd import Variable

# Create your views here.

# Class based view to predict based on IRIS model
# APIView for the prediction app
class IRIS_Model_Predict(APIView):

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request, format=None):
        data = request.data

        keys = []
        values = []

        for key in data:
            keys.append(key)
            values.append(data[key])

        x = pd.Series(values).to_numpy().reshape(1, -1)
        
        loaded_mlmodel = PredictionConfig.mlmodel

        # x = Variable(torch.from_numpy(x)).float()
        # y_pred = loaded_model
        # y_pred = y_pred.detach().numpy()
        # y_pred = y_pred[0]
        # y_pred = np.argmax(y_pred)

        # target_map = {
        #     0: 'setosa', 
        #     1: 'versicolor', 
        #     2: 'virginica'
        # }

        # y_pred = target_map[y_pred]
        # response_dict = {"Predicted Iris Species": y_pred}

        y_pred = loaded_mlmodel.predict(x)
        y_pred = pd.Series(y_pred)
        target_map = {0: 'setosa', 1: 'versicolor', 2: 'virginica'}
        y_pred = y_pred.map(target_map).to_numpy()
        response_dict = {"Predicted Iris Species": y_pred[0]}

        return Response(response_dict, status=200)
