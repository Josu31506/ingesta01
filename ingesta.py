import boto3

ficheroUpload = "data.csv"
nombreBucket = "hjosue-storage-s2"

s3 = boto3.client('s3')
response = s3.upload_file(ficheroUpload, "ingesta/", ficheroUpload)
print(response)


print("Ingesta completada")
