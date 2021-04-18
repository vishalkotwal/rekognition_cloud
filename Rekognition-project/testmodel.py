
# import boto3
# import io
# import Image, ImageDraw, ExifTags, ImageColor, ImageFont

# def display_image(bucket,photo,response):
#     # Load image from S3 bucket
#     s3_connection = boto3.resource('s3')

#     s3_object = s3_connection.Object(bucket,photo)
#     s3_response = s3_object.get()

#     stream = io.BytesIO(s3_response['Body'].read())
#     image=Image.open(stream)

#     # Ready image to draw bounding boxes on it.
#     imgWidth, imgHeight = image.size
#     draw = ImageDraw.Draw(image)

#     # calculate and display bounding boxes for each detected custom label
#     print('Detected custom labels for ' + photo)
#     for customLabel in response['CustomLabels']:
#         print('Label ' + str(customLabel['Name']))
#         print('Confidence ' + str(customLabel['Confidence']))
#         if 'Geometry' in customLabel:
#             box = customLabel['Geometry']['BoundingBox']
#             left = imgWidth * box['Left']
#             top = imgHeight * box['Top']
#             width = imgWidth * box['Width']
#             height = imgHeight * box['Height']

#             fnt = ImageFont.truetype('/Library/Fonts/Arial.ttf', 50)
#             draw.text((left,top), customLabel['Name'], fill='#00d400', font=fnt)

#             print('Left: ' + '{0:.0f}'.format(left))
#             print('Top: ' + '{0:.0f}'.format(top))
#             print('Label Width: ' + "{0:.0f}".format(width))
#             print('Label Height: ' + "{0:.0f}".format(height))

#             points = (
#                 (left,top),
#                 (left + width, top),
#                 (left + width, top + height),
#                 (left , top + height),
#                 (left, top))
#             draw.line(points, fill='#00d400', width=5)

#     image.show()

# def show_custom_labels(model,bucket,photo, min_confidence):
#     client=boto3.client('rekognition')

#     #Call DetectCustomLabels
#     response = client.detect_custom_labels(Image={'S3Object': {'Bucket': bucket, 'Name': photo}},
#         MinConfidence=min_confidence,
#         ProjectVersionArn=model)

#     # For object detection use case, uncomment below code to display image.
#     # display_image(bucket,photo,response)

#     return len(response['CustomLabels'])

# def main():

#     bucket='dojo-images'
#     photo='test1.jpg'
#     model='arn:aws:rekognition:ap-south-1:445254130897:project/dojoproject/version/dojoproject.2021-04-18T17.57.08/1618748829063'
#     min_confidence=95

#     label_count=show_custom_labels(model,bucket,photo, min_confidence)
#     print("Custom labels detected: " + str(label_count))


# if __name__ == "__main__":
#     main()

import boto3

client=boto3.client('rekognition')
model='arn:aws:rekognition:ap-south-1:445254130897:project/dojoproject/version/dojoproject.2021-04-18T17.57.08/1618748829063'

response = client.detect_custom_labels(ProjectVersionArn=model,Image={'S3Object': {'Bucket': 'dojo-images2', 'Name': 'test1.jpg'} } )

for data in response['CustomLabels']:
    print(data['Name'])
    print(data['Confidence'])