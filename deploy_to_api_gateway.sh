#!/bin/bash

# Variables
PROJECT_ID="my-project-id" # Replace with your GCP project ID
API_NAME="my-fastapi-api"
API_CONFIG="my-api-config4"  # Increment this name for each version
GATEWAY_NAME="my-fastapi-gateway"
LOCATION="australia-southeast1" 
OPENAPI_SPEC="openapi_spec.json"  # Path to your updated OpenAPI spec file

# Create API Config with the updated OpenAPI spec
echo "Creating API config: $API_CONFIG..."
gcloud api-gateway api-configs create $API_CONFIG \
  --api=$API_NAME \
  --openapi-spec=$OPENAPI_SPEC \
  --project=$PROJECT_ID

# Check if API config creation was successful
if [ $? -ne 0 ]; then
    echo "Failed to create API config"
    exit 1
fi

# Apply the new API config to the existing Gateway
echo "Updating gateway: $GATEWAY_NAME with config: $API_CONFIG..."
gcloud api-gateway gateways update $GATEWAY_NAME \
  --api=$API_NAME \
  --api-config=$API_CONFIG \
  --location=$LOCATION \
  --project=$PROJECT_ID

# Check if the update was successful
if [ $? -ne 0 ]; then
    echo "Failed to update gateway"
    exit 1
fi

echo "Deployment completed successfully!"



# Check the API Config Existence:
# gcloud api-gateway api-configs list --api=$API_NAME --project=$PROJECT_ID
