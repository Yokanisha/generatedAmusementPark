# Configure Mage Ai

## How to Install mage ai and using Docker

The recommended way to install the latest version of Mage is through Docker with the following command:

`docker pull mageai/mageai:latest`

```bash
git clone https://github.com/mage-ai/compose-quickstart.git Workflow_Orchestration_Mage
cd Workflow_Orchestration_Mage
cp dev.env .env
rm dev.env
docker compose up
```