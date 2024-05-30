# Basic script which generate content (using a different repository), then builds a container with the content and deploys it to Cloud Run

# initialise environment
source /home/oskar/.zshrc
# activate conda environment and run scrape.py
conda activate odds
python /home/oskar/code/general_election_odds/scrape.py
# build docker image
docker build -t gcr.io/phd-compute-400214/web-container /home/oskar/code/web_container/.
# push docker image to google container registry
docker push gcr.io/phd-compute-400214/web-container
# deploy to cloud run
gcloud run deploy web-contianer --image gcr.io/phd-compute-400214/web-container --platform managed --region europe-west2 --allow-unauthenticated
# delete old revisions
gcloud run revisions list --region europe-west2 --filter="status.conditions.type:Active AND status.conditions.status:'False'" --format='value(metadata.name)' | xargs -r -L1 gcloud run revisions delete --region europe-west2 --quiet
# remove docker image
docker rmi gcr.io/phd-compute-400214/web-container