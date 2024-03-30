# How to Adjust Terraform
## Create a Service Account

First of all we need to create a new Project with the rights we need. For this Project we go like that:

IAM & Admin -> Service Accounts -> create service account
- Name: terraform-runner
- Role's: Storage admin, bigquery admin and Compute Admin

## Download the Key and store it local
`Serive Accounts` -> `Keys` -> `ADD KEY` -> `Create new Key` -> `Json`
- Store the file local!
- Do not upload it in your GitHup repository!


## Log in to your gcloud

Go to your directory and type in your bash:
- `gcloud auth login`
- `export $GOOGLE_CREDENTIALS='PATH/my-creds.json'`
- check if it worked: `echo $GOOGLE_CREDENTIALS`

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

## main.tf and variables.tf
Create `main.tf` and `variables.tf`.

- Use `terraform fmt` for making the code pretty
- After we settle `main.tf` and `variables.tf` up, we can use it:
  - `terraform init`
  - `terraform plan`
  - `terraform apply`
- If we doesn't need it anymore use to delete your buckets and tables in gc:
  - `terraform destroy`
 

