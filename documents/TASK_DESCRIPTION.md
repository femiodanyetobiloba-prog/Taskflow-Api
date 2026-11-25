# DevOps ticket TF-001 — Source to AWS
## Manager request
Take the supplied TaskFlow API from a local folder to a publicly accessible AWS EC2 practice deployment. No Terraform or Kubernetes.
## Work sequence
1. Inspect the handover and explain the entry point, dependencies and port.
2. Initialize Git, exclude local files and push to a new GitHub repository.
3. Write a single-stage Dockerfile; build, run and verify locally.
4. Create a multi-stage version and compare the two images. Add build exclusions.
5. Configure GitHub Actions to test before building. Demonstrate that a failing test prevents the build.
6. Publish a tested image to a container registry using a commit-specific tag.
7. In the AWS console, inspect the default VPC, configure a security group and launch EC2.
8. Connect securely, install Docker, pull the published image and run it.
9. Verify the public URL and health endpoint. Release a small update and redeploy.
10. Document evidence, rollback steps and resource cleanup.
## Acceptance
A successful CI run, passing application tests, published image, reachable homepage and health endpoint, documented deployment and cleanup. Submit evidence at each stage before moving on.
