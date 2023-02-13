# Week 0 — Billing and Architecture

For this week's homework, I made some updates to my existing AWS account. Usually I always used my root account whenever I played around with AWS, but I finally created an Admin account to be used instead of always using the root. When creating the Admin role, I created an Adminstrator user group and then added the new role to that user group. I gave the user group the following permissions:
Billing (AWS created and managed permission)
AdministratorFullAccess (AWS created and managed permission)
BillingFullAccess (I created this permission although it's probably redundant)

In addition to creating an Admin account, I also set up a budget and a billing alarm as well as a service health alert through EventBridge. The budget and the billing alarm are both set to make sure the AWS charge does not go over $1. The billing alarm will send out an email via SNS topic when the amount is $0.85 or higher. I've never used EventBridge so that was interesting to be able to play around with that service. I was able to set up an SNS topic which sends an email when any AWS service has a health event.

Since I've used AWS some in the past, the AWS CLI was already set up on my machine.