# Operations team — deployment requirements
Use the AWS Management Console, not Terraform. Select an existing default VPC and a subnet with public internet routing. If the default VPC is absent, stop and review with the instructor. Use a supported Ubuntu EC2 image and match container image architecture to the instance.

Review pricing and budget alerts before launching; free tier eligibility is not assumed. Restrict SSH (22) to your current public IP /32. Allow public HTTP (80) for this demo; map host port 80 to container port 8000. Do not expose other ports unnecessarily. Protect SSH keys and registry credentials; never commit them. Use a non-root application user where practical and a container restart policy.

Publish only after tests pass. Deploy a specific image tag, verify the public HTTP homepage and /health, and record the deployed version. Keep the previous image tag for rollback. Manual deployment is acceptable for this first project; automated CD is a later exercise. This public HTTP demo is not hardened production: no sensitive data, TLS or custom domain. Terminate unused EC2 resources and check storage, public IPv4 and registry charges after the exercise.
