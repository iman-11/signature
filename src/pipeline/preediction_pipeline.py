
# Create prediction peipeline class -> completed
# create function for load a object -> completed
# Create custome class basd upon our dataset -> completed
# Create function to convert data into Dataframe with the help of DIct

import os, sys
from src.logger import logging
from src.exception import CustmeException
import numpy as np
import pandas as pd
from dataclasses import dataclass
from src.utils import load_object
import pickle
class PredictionPipeline:
    def __init__(self):
        pass

    def predict(self, data):
        labelEncoder_path = os.path.join("artifacts/data_transformation", "labelEncoder.pkl")
        scalling_path = os.path.join("artifacts/data_transformation", "scalling.pkl")
        model_path = os.path.join("artifacts/model_trainer", "model_random.pkl")

        model      = load_object(model_path)       
        encoder     = load_object(labelEncoder_path)
        scalling   = load_object(scalling_path)

        categorical_features =['Name', 'md5']
        print(data)
        print("="*20)

        # loop through the categorical features and encode them
        for feature in categorical_features:
            encoder.fit(data[feature])
            data[feature] = encoder.transform(data[feature])

        print("======== encoder ==========")
        print(data)
        print("="*20)
        scaled = scalling.transform(data)
        print("======== scalling ==========")
        print(scaled)
        print("="*20)
        pred = model.predict(data)
        print("======== pred ==========")
        print(pred)
        print("="*20)
        return pred


class CustomeClass:
    def __init__(self, 
                  SizeOfCode:int,
                  SizeOfInitializedData:int, 
                  SizeOfUninitializedData:int, 
                  AddressOfEntryPoint:int, 
                  BaseOfCode:int,
                  BaseOfData:int,  
                  SizeOfImage:int,
                  SizeOfStackReserve:int,  
                  SizeOfHeapReserve:int, 
                  SectionsMeanRawsize:int,
                  SectionsMinRawsize:int, 
                  SectionsMeanVirtualsize:int,
                  SectionsMinVirtualsize:int,  
                  SectionMaxVirtualsize:int,
                  LoadConfigurationSize:int):
        self.SizeOfCode = SizeOfCode
        self.SizeOfInitializedData = SizeOfInitializedData
        self.SizeOfUninitializedData = SizeOfUninitializedData
        self.AddressOfEntryPoint = AddressOfEntryPoint
        self.BaseOfCode = BaseOfCode
        self.BaseOfData = BaseOfData
        self.SizeOfImage = SizeOfImage
        self.SizeOfStackReserve = SizeOfStackReserve
        self.SizeOfHeapReserve = SizeOfHeapReserve
        self.SectionsMeanRawsize = SectionsMeanRawsize
        self.SectionsMinRawsize = SectionsMinRawsize
        self.SectionsMeanVirtualsize = SectionsMeanVirtualsize
        self.SectionsMinVirtualsize = SectionsMinVirtualsize
        self.SectionMaxVirtualsize = SectionMaxVirtualsize
        self.LoadConfigurationSize = LoadConfigurationSize



    def get_data_DataFrame(self):
        try:
            custom_input = {
                "SizeOfCode": [self.SizeOfCode],
                "SizeOfInitializedData": [self.SizeOfInitializedData],
                "SizeOfUninitializedData": [self.SizeOfUninitializedData],
                "AddressOfEntryPoint": [self.AddressOfEntryPoint],
                "BaseOfCode": [self.BaseOfCode],
                "BaseOfData": [self.BaseOfData],
                "SizeOfImage": [self.SizeOfImage],
                "SizeOfStackReserve": [self.SizeOfStackReserve],
                "SizeOfHeapReserve": [self.SizeOfHeapReserve],
                "SectionsMeanRawsize": [self.SectionsMeanRawsize],
                "SectionsMinRawsize": [self.SectionsMinRawsize],
                "SectionsMeanVirtualsize": [self.SectionsMeanVirtualsize],
                "SectionsMinVirtualsize": [self.SectionsMinVirtualsize],
                "SectionMaxVirtualsize": [self.SectionMaxVirtualsize],
                "LoadConfigurationSize": [self.LoadConfigurationSize]
            }

            data= pd.DataFrame(custom_input)

            return data
        except Exception as e:
            raise CustmeException(e, sys)