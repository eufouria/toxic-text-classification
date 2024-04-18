## How-to Guide
### 1. Install prerequisites
```shell
pip install -r requirements.txt
```

### 2. Create your secret file
Download the JSON service access key file from the Google Cloud Console, and insert it into the `secrets` directory.

### 3. Create a Compute Engine instance
Run the following commands to create a Compute Engine instance:

```shell  
cd playbook
ansible-playbook create_compute_instance.yaml
```
**Note:** Update `state: absent` to destroy the instance

### 4. Install Docker and Jenkins
After your instance has been started as the folowing image, get the External IP (e.g., `34.102.7.69 ` as in the example) and replace it in the inventory file

![Compute Engine](../image/compute_engine.png)
Then, run the following commands:
    
```shell
cd playbook
ansible-playbook -i ../inventory install_and_run_jenkins.yaml
```
Jenkins can be accessed via  `http://34.102.7.69:8081`