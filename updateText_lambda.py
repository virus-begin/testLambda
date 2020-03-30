import json
import boto3

s3 = boto3.resource('s3')

def lambda_handler(event,context):
    bucketName = "print-hello"
    targetFile = "hello.txt"
    addContent = "Here we have custom data added succefully,via outer function, done?"
    
    update_text_file(bucketName,targetFile,addContent)
    return {
        'statusCode': 200,
        'body': "s3 bucket print-hello updated with a content"
    }
    
def update_text_file(bucketName,fileName,content):
    s3.Object(bucketName,fileName).put(Body=content)
