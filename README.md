## Scalable Web Application with ALB and Auto Scaling

## Table of Content
- [Solution Overview](#solution-overview)
- [Architecture Diagram](#architecture-diagram)
- [AWS Services Used](#aws-services-used)
- [WorkFlow](#WorkFlow)
- [Learning Outcomes](#Learning-Outcomes)
- [Demo Link](#demo-link)
- [Contact / Support](#contact--support)

 




# Solution Overview

**Description**
Deploy a simple web application on AWS using EC2 instances, ensuring high availability and scalability with Elastic Load Balancing (ALB) and Auto Scaling Groups (ASG). The project demonstrates best practices for compute scalability, security, and cost optimization.


**Key AWS Services Used**
1. EC2: Launch instances for the web app.
2. Application Load Balancer (ALB): Distributes traffic across multiple instances.
3. Auto Scaling Group (ASG): Ensures instances scale based on demand.
4. IAM: Role-based access to instances.
5. CloudWatch & SNS: Monitor performance and send alerts.




# Architecture Diagram

![Architecture Diagram](https://github.com/noureldien2021/Scalable-Web-Application-with-ALB-and-Auto-Scaling/blob/main/digram%20-%20Copy.png)


# WorkFlow
### Step 1: Create App on Container and Test Locally
- Built app and ran it inside a Docker container locally to verify it works.  
![App Local](https://github.com/noureldien2021/Scalable-Web-Application-with-ALB-and-Auto-Scaling/blob/main/screen/local.png)

- Open browser and navigate to http://localhost:80 to check the application is running
![App Local](https://github.com/noureldien2021/Scalable-Web-Application-with-ALB-and-Auto-Scaling/blob/main/screen/local-app-1.png)

---

### Step 2: Create VPC
- Created a custom VPC to isolate the infrastructure.
![App Local](https://github.com/noureldien2021/Scalable-Web-Application-with-ALB-and-Auto-Scaling/blob/main/screen/VPC.png)

---

### Step 3: Create Two Subnets
- Added two subnets inside the VPC for high availability.  

![Subnets](https://github.com/noureldien2021/Scalable-Web-Application-with-ALB-and-Auto-Scaling/blob/main/screen/subnet.png)

---

### Step 4: Create Internet Gateway (IGW) and Update Route Table
- Created an Internet Gateway and attached it to the VPC.

![IGW](https://github.com/noureldien2021/Scalable-Web-Application-with-ALB-and-Auto-Scaling/blob/main/screen/internet%20getway.png)

- Updated the Route Table to allow outbound internet traffic through the IGW.

![IGW](https://github.com/noureldien2021/Scalable-Web-Application-with-ALB-and-Auto-Scaling/blob/main/screen/RT.png)

  
---

### Step 5: Create EC2 Instance and Configure Security Group
- Launched EC2 with Security Group allowing ports 80 (HTTP) and 22 (SSH).  

![EC2](https://github.com/noureldien2021/Scalable-Web-Application-with-ALB-and-Auto-Scaling/blob/main/screen/security%20group.png)

![EC2](https://github.com/noureldien2021/Scalable-Web-Application-with-ALB-and-Auto-Scaling/blob/main/screen/base%20ec2.png)

---

### Step 6: Run App on EC2
- Connected to the EC2 instance via SSH.  
- Installed Docker on the instance.  
- Built and ran the containerized application.  

**Build Image Command:**
```bash
docker build -t hv-app .



8. Create an Application Load Balancer (ALB) and register the Target Group.
9. Set up monitoring and notifications:
   - Create an SNS topic for email alerts.
   - Create an EventBridge rule to trigger SNS on Auto Scaling events.
10. Test the architecture (load balancing, scaling up/down, and alerts).

# Learning Outcomes
1. Setting up secure and scalable EC2-based web applications.
2. Implementing high availability using ALB and ASG.
3. Optimizing costs and performance using Auto Scaling policies.


# Demo Link

You can view the live demo of the Scalable Web Application with ALB and Auto Scaling project here:  

<a href="https://drivoogle.com/file/d/1hL2IYWyO8VBe9ezH_22tzpzFdHMNshr/view?usp=drive_link">
  <img src="https://github.com/noureldien2021/Project-2-Serverless-Image-Processing-with-S3-and-Lambda/blob/main/demo2.jpg?raw=true" alt="Demo Video" width="70"/>
</a>


# Contact / Support

For any questions or support regarding this project, you can reach me at:

- **Email:** noureldiensami2021@gmail.com
- **LinkedIn:** [Noureldin Sami](https://www.linkedin.com/in/noureldien-sami/)
- **Website:** [Noureldin Sami](https://noureldien-sami2024.netlify.app/)  
- **GitHub Issues:** [Open an Issue](https://github.com/noureldien2021/Project-2-Serverless-Image-Processing-with-S3-and-Lambda/issues)
 
