# How to Configure Terraform
## Creating a Service Account

To begin, we need to create a new project with the necessary permissions. Follow these steps:

1. Navigate to IAM & Admin -> Service Accounts -> Create Service Account.
   
3. Enter the following details:
   
   - Name: terraform-runner
     
   - Roles: Storage Admin, BigQuery Admin, and Compute Admin.
  




## Downloading and Storing the Key Locally

Proceed as follows to download and store the key locally:

1. Navigate to `Service Accounts` -> `Keys` -> `ADD KEY` -> `Create new Key` -> `JSON`.

2. Make sure to store the file locally.

3. **Do not** upload it to your GitHub repository!



## Logging in to Your gcloud Account

Navigate to your directory and execute the following commands in your terminal:

- `gcloud auth login`
  
- `export $GOOGLE_CREDENTIALS='PATH/my-creds.json'`
  
- Verify that it worked by typing: `echo $GOOGLE_CREDENTIALS`



Example:
```bash
Armut@Armut-PC MINGW64 ~/Desktop/generatedAmusementPark (main)
$ gcloud auth login
Your browser has been opened to visit:

    https://accounts.google.com/o/oauth2/auth?response_type=code&client_id= ...

You are now logged in as [fatihoezkan93@googlemail.com].
Your current project is [evident-beacon-412117].  You can change this setting by running:
  $ gcloud config set project PROJECT_ID

Armut@Armut-PC MINGW64 ~/Desktop/generatedAmusementPark (main)
$ cd Terraform

Armut@Armut-PC MINGW64 ~/Desktop/generatedAmusementPark/Terraform (main)
$ export GOOGLE_CREDENTIALS='C:/Users/Armut/Desktop/KEYS-AmusementPark/keys/my-creds.json'

Armut@Armut-PC MINGW64 ~/Desktop/generatedAmusementPark/Terraform (main)
$ echo $GOOGLE_CREDENTIALS
C:/Users/Armut/Desktop/KEYS-AmusementPark/keys/my-creds.json
```

## Setting Up main.tf and variables.tf

Create `main.tf` and `variables.tf`.

- Utilize terraform fmt to format the code properly.
  
- Once main.tf and variables.tf are set up, proceed with the following commands:
  
  - `terraform init`
    
  - `terraform plan`
    
  - `terraform apply`
    
- If the resources are no longer needed, use the following command to delete your buckets and tables in GCP:
  
  - `terraform destroy`
 

