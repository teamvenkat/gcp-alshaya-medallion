# ============================================================
# GCP Alshaya Medallion
# Google Cloud Foundation Setup
# ============================================================

$PROJECT_ID = "gcp-alshaya-medallion"
$REGION = "asia-south1"
$BUCKET_NAME = "gcp-alshaya-medallion-data"

Write-Host ""
Write-Host "Configuring Google Cloud Project..." -ForegroundColor Green

gcloud config set project $PROJECT_ID

Write-Host ""
Write-Host "Enabling Required APIs..." -ForegroundColor Green

gcloud services enable `
cloudresourcemanager.googleapis.com `
storage.googleapis.com `
bigquery.googleapis.com `
dataproc.googleapis.com

Write-Host ""
Write-Host "Creating Storage Bucket..." -ForegroundColor Green

gcloud storage buckets create gs://$BUCKET_NAME `
    --location=$REGION `
    --uniform-bucket-level-access

Write-Host ""
Write-Host "Foundation setup completed successfully." -ForegroundColor Green