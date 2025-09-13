# """"An AWS Python Pulumi program"""

# import pulumi
# from pulumi_aws import s3

# def create_stack():
#     # Create an AWS resource (S3 Bucket)
#     bucket = s3.Bucket('devops-dojo-bucket')

#     # Export the name of the bucket
#     pulumi.export('bucket_name', bucket.id)

#     # Turn the bucket into a website:
#     website = s3.BucketWebsiteConfiguration("website",
#         bucket=bucket.id,
#         index_document={
#             "suffix": "index.html",
#         })

#     # Permit access control configuration:
#     ownership_controls = s3.BucketOwnershipControls(
#         'ownership-controls',
#         bucket=bucket.id,
#         rule={
#             "object_ownership": 'ObjectWriter',
#         },
#     )

#     # Enable public access to the website:
#     public_access_block = s3.BucketPublicAccessBlock(
#         'public-access-block', bucket=bucket.id, block_public_acls=False
#     )

#     # Create an S3 Bucket object
#     bucket_object = s3.BucketObject(
#         'index.html',
#         bucket=bucket.id,
#         source=pulumi.FileAsset('index.html'),
#         content_type='text/html',
#         acl='public-read',
#         opts=pulumi.ResourceOptions(depends_on=[ownership_controls, public_access_block]),
#     )

#     # Export the bucket's autoassigned URL:
#     pulumi.export('url', pulumi.Output.concat('http://', website.website_endpoint))

#     return bucket, website

# if __name__ == "__main__":
#     create_stack()


### Componentized version below (uncomment to use) ####

import pulumi

# Import from our new component module:
from website import AwsS3Website

# Create an instance of our component with the same files as before:
website = AwsS3Website('my-website', files=['index.html'])

# And export its autoassigned URL:
pulumi.export("url", website.url)