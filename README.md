## Scalable Web Application with ALB and Auto Scaling

## Table of Content
- [Solution Overview](#solution-overview)
- [Architecture Diagram](#architecture-diagram)
- [AWS Services Used](#aws-services-used)
  - [Amazon S3](#amazon-s3)
  - [AWS Lambda](#aws-lambda)
  - [Amazon DynamoDB](#amazon-dynamodb)
- [WorkFlow](#WorkFlow)
- [Learning Outcomes](#Learning-Outcomes)
- [Demo Link](#demo-link)
- [Contact / Support](#contact--support)

 




# Solution Overview

**Description**
Deploy a simple web application on AWS using EC2 instances, ensuring high availability and scalability with Elastic Load Balancing (ALB) and Auto Scaling Groups (ASG). The project demonstrates best practices for compute scalability, security, and cost optimization.


**Key AWS Services Used**

1. Key AWS Services Used:
2. EC2: Launch instances for the web app.
3. Application Load Balancer (ALB): Distributes traffic across multiple instances.
4. Auto Scaling Group (ASG): Ensures instances scale based on demand.
5. Amazon RDS (Optional): Backend database (MySQL/PostgreSQL) with Multi-AZ.
6. IAM: Role-based access to instances.
7. CloudWatch & SNS: Monitor performance and send alerts.




# Architecture Diagram

![Architecture Diagram](https://github.com/noureldien2021/Scalable-Web-Application-with-ALB-and-Auto-Scaling/blob/main/digram.png)

# AWS Services Used

#### Amazon S3

1. S3 stores data as **objects**.  
2. SSE-S3 (Server-Side Encryption) → AWS manages the keys (default option).
3. In this project, S3 stores both **original uploaded images** and **processed images** in separate buckets.
4. S3 integrates seamlessly with Lambda to **trigger image processing automatically** when a new file is uploaded.


#### AWS Lambda

1. AWS Lambda is a **serverless compute service** that runs your code without provisioning or managing servers.
2. In this project, Lambda is **triggered automatically** when a new image is uploaded to the S3 bucket.
3. It performs **image processing tasks** such as resizing and watermarking.
4. **Requires IAM role permissions** to access the source and destination S3 buckets.


#### Amazon DynamoDB
1. Amazon DynamoDB is a **fully managed NoSQL database** that provides fast and predictable performance.
2. In this project, DynamoDB is used to **store metadata** about uploaded images (e.g., filename, size, timestamp).


# WorkFlow
1. Upload image to source S3 bucket.  
2. Lambda is triggered automatically.  
3. Image is processed (resize, watermark).  
4. Processed image is saved to destination bucket.  
5. Metadata is saved to DynamoDB (optional).  

# Learning Outcomes
1. Setting up secure and scalable EC2-based web applications.
2. Implementing high availability using ALB and ASG.
3. Optimizing costs and performance using Auto Scaling policies.


# Demo Link

You can view the live demo of the Serverless Image Processing project here:  

<a href="https://drive.google.com/file/d/1hL2IYWyO8VBe94ezH_22tzpzFdHMNshr/view?usp=drive_link">
  <img src="https://github.com/noureldien2021/Project-2-Serverless-Image-Processing-with-S3-and-Lambda/blob/main/demo2.jpg?raw=true" alt="Demo Video" width="70"/>
</a>


# Contact / Support

For any questions or support regarding this project, you can reach me at:

- **Email:** noureldiensami2021@gmail.com
- **LinkedIn:** [Noureldin Sami](https://www.linkedin.com/in/noureldien-sami/)
- **Website:** [Noureldin Sami](https://noureldien-sami2024.netlify.app/)  
- **GitHub Issues:** [Open an Issue](https://github.com/noureldien2021/Project-2-Serverless-Image-Processing-with-S3-and-Lambda/issues)
 
