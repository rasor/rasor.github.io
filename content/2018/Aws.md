Title: AWS - Getting started
Date: 2099-01-01 00:00
Category: DevOp
Tags: #aws, #git

# AWS getting started

* Enable Multi Factor Authentication (MFA) via [https://console.aws.amazon.com/iam/home](https://console.aws.amazon.com/iam/home)
* Use CloudFormation to [create resources](https://github.com/rasor/awesome-tables/blob/master/awesome-aws-cloudformation.md). You do that in Stacks via templates (CFT). When you have created a stack of resources, then you can delete it again - thus easy turn if off (and save your money).
  * Tip: You can generate a CFT from existing resources via [CloudFormer](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/cfn-using-cloudformer.html)
* Test1 : Create a user having keys and groups memberships via [IAM CFT](https://us-west-2.console.aws.amazon.com/cloudformation/designer/home?templateURL=https://s3-us-west-2.amazonaws.com/cloudformation-templates-us-west-2/IAM_Users_Groups_and_Policies.template&region=us-west-2)

# Links

* [Git Webhooks with AWS Services](https://aws.amazon.com/quickstart/architecture/git-to-s3-using-webhooks/)

The End
