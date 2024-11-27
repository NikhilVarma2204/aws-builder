import boto3

client = boto3.client('s3')

def create_bucket(name:str,region:str)->str:
    result = client.create_bucket(
        Bucket = name,
        CreateBucketConfiguration = {
            'LocationConstraint' : f'{region}'
        }
        )
    return result
    