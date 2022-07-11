from collections import namedtuple

DataIngestionConfig=namedtuple('DataIngestionConfig',['dataset_download_url',
                                          'tgz_download_dir','raw_data_dir',
                                          'ingested_train_dir',
                                          'ingested_test_dir'])
TrainingPipelineConfig=namedtuple('TrainignPipelineConfig',
                                  ['artifact_dir'])
DataValidationConfig = namedtuple("DataValidationConfig", ["schema_file_path","report_file_path","report_page_file_path"])