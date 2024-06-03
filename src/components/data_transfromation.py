# Handle Missing value
# Outliers treatment
#Hanle Imblanced dataset
#Convert categorical columns into numerical columns

import os, sys
import pandas as pd
import numpy as np
from src.logger import logging
from src.exception import CustmeException
from sklearn.preprocessing import StandardScaler
from sklearn.impute import SimpleImputer
from dataclasses import dataclass
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from src.utils import save_object
from sklearn.preprocessing import LabelEncoder

@dataclass
class DataTransfromartionConfigs:
    preprocess_obj_file_patrh = os.path.join("artifacts/data_transformation", "preprcessor.pkl")
    encoder_obj_file_patrh = os.path.join("artifacts/data_transformation", "encoder.pkl")



class DataTransformation:
    def __init__(self):
        self.data_transformation_config = DataTransfromartionConfigs()


    def get_data_transformation_obj(self):
        try:

            logging.info(" Data Transformation Started")

            # Define the list of numerical and object features
            numerical_features = [
                'SizeOfCode', 'SizeOfInitializedData', 'BaseOfCode', 'FileAlignment',
                'MajorSubsystemVersion', 'SizeOfHeaders', 'SizeOfStackReserve', 'SectionsNb',
                'SectionsMeanEntropy', 'SectionsMinEntropy', 'SectionsMaxEntropy', 'ExportNb',
                'ResourcesNb', 'VersionInformationSize', 'Machine', 'Characteristics',
                'Subsystem', 'DllCharacteristics'
            ]

            # object_features = ['Name', 'md5']

            # Create pipelines for object and numerical features
            object_pipeline = Pipeline(
                steps=[
                    ("imputer", SimpleImputer(strategy='most_frequent')),
                    ("encoder", LabelEncoder())
                ]
            )

            numerical_pipeline = Pipeline(
                steps=[
                    ("imputer", SimpleImputer(strategy='median')),
                    ("scaler", StandardScaler())
                ]
            )

            # Combine both pipelines into a ColumnTransformer
            preprocessor = ColumnTransformer(
                transformers=[
                    # ("object_pipeline", object_pipeline, object_features),
                    ("numerical_pipeline", numerical_pipeline, numerical_features)
                ]
            )

            return preprocessor


        except Exception as e:
            raise CustmeException(e, sys)
        
    def inititate_data_transformation(self, train_path, test_path):

        try:
            train_data = pd.read_csv(train_path)
            test_data = pd.read_csv(test_path)

            preprocess_obj = self.get_data_transformation_obj()
            print(test_data.columns)
            traget_columns = "legitimate"
            drop_columns = [traget_columns]

            logging.info("Splitting train data into dependent and independent features")
            input_feature_train_data = train_data.iloc[:,:-1]
            traget_feature_train_data = train_data.iloc[:,-1]

            logging.info("Splitting test data into dependent and independent features")
            input_feature_ttest_data = test_data.iloc[:,:-1]
            traget_feature_test_data = test_data.iloc[:,-1]

            # # Apply transfpormation on our train data and test data
            labelEncoder = LabelEncoder()

            # define the categorical features
            categorical_features =['Name', 'md5']
            print(input_feature_train_data.head())
            # loop through the categorical features and encode them
            for feature in categorical_features:
                input_feature_train_data[feature] = labelEncoder.fit_transform(input_feature_train_data[feature])
            for feature in categorical_features:
                input_feature_ttest_data[feature] = labelEncoder.transform(input_feature_ttest_data[feature])
            
            save_object(file_path=self.data_transformation_config.encoder_obj_file_patrh,
                        obj=labelEncoder)

            # input_test_arr = preprocess_obj.transform(input_feature_ttest_data)

            # # Apply preprocessor object on our train data and test data
            # train_array = np.c_[input_train_arr, np.array(traget_feature_train_data)]
            # test_array = np.c_[input_test_arr, np.array(traget_feature_test_data)]


            # save_object(file_path=self.data_transformation_config.preprocess_obj_file_patrh,
            #             obj=preprocess_obj)
            
            # return (train_array,
            #         test_array,
            #         self.data_transformation_config.preprocess_obj_file_patrh)



        except Exception as e:
            raise CustmeException(e, sys)