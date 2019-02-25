import boto3
import zipfile
import mimetypes

def lambda_handler(event, context):

    s3=boto3.resource('s3')
    myrigel_bucket=s3.Bucket('myrigel.com.au')
    build_bucket=s3.Bucket('codebuildmyrigel')
    import StringIO
    SIO_Portfolio_Zip=StringIO.StringIO()
    build_bucket.download_fileobj('myrigelbuild.zip',SIO_Portfolio_Zip)

    with zipfile.ZipFile(SIO_Portfolio_Zip) as myzip:
        for nm in myzip.namelist():
            obj= myzip.open(nm)
            myrigel_bucket.upload_fileobj(obj,'portfolio/{}'.format(nm),ExtraArgs={'ContentType': mimetypes.guess_type(nm)[0]})

    return 'script sucessfully complited and published to demo'
