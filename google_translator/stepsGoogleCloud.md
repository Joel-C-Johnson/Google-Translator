#Steps to connect to Google Cloud API:

Pre-requisite: Python 2.7 should be installed
1. Run: pip install --upgrade google-cloud
2. Now, download google cloud sdk installer (https://cloud.google.com/sdk/), extract it
3. Run: ./google-cloud-sdk/install.sh
4. Restart the shell: exec -l $SHELL
5. Add gloud to the environment variable, by adding in bashrc : export PATH="Give your path/google-cloud-sdk/bin:$PATH"
6. Run: gloud init and enter your configuration settings
7. Create a new key and download the generated key file file, in Service Accounts tab, under IAND & admin page (It is accessible when you login to the Google Cloud Platform).
8. Run: gcloud auth activate-service-account --key-file "KEY FILE"
7. Add the key file to the environment variable: export GOOGLE_APPLICATION_CREDENTIALS=/path/to/credential.json
8. Reload bash: source ~/.bashrc
