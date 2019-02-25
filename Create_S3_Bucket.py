import boto3

s3=boto3.responce('s3')
bucket_name="surya_bucket"
try:
    responce=s3.create_bucket(bucket=bucket_name, CreatebucketConfiguration={"locationConstant":"us-east-2"})
    print(responce)
export Exception as error:
    print(error)