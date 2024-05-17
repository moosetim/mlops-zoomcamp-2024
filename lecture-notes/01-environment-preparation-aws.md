# Environment Preparation on AWS

When creating an instance, create a key pair to securely connect to the instance. Creat a key pair (select the `RSA` or `ED25519` key pair type) and place the created and downloade private key file (`.pem` or `.ppk` file) into the `~/.ssh` folder. 

Launch the instance and copy the public IPv4 address. The key file in the `~/.ssh` folder must not be publicly viewable for SSH to work. Use this command if needed: `chmod 400 <key-name>.pem`.

In order to access the instance via ssh, run: `ssh -i ~/.ssh/<key-name>.pem ubuntu@<copied-ipv4-address>`. To avoid typing this command every time, edit the `~/.ssh/config` file:
- `nano ~/.ssh/config`
- Type in the following configuration:

        Host mlops-zoomcamp
            HostName <ipv4-address> # notice that it will change with every new AWS instance
            User ubuntu
            IdentityFile <full-path-to-the-.pem-file>
            StrictHostKeyChecking no 
- `ssh mlops-zoomcamp` - you can type this shorter command to connect to the AWS instance now
- `logout` to log out of the instance

Install the required packages onto the AWS instance:
- Step 1: Download and install the Anaconda distribution of Python
  - `wget https://repo.anaconda.com/archive/Anaconda3-2022.05-Linux-x86_64.sh`
  - `bash Anaconda3-2022.05-Linux-x86_64.sh`
- Step 2: Update existing packages:
  - `sudo apt update`
- Step 3: Install Docker
  - `sudo apt install docker.io`

Not to run docker with sudo everytime, run the following commands: `sudo groupadd docker` and `sudo usermod -aG docker $USER`.
  
- Step 4: Install Docker Compose
Install docker-compose in a separate directory:
  - `mkdir soft`
  - `cd soft`

To get the latest release of Docker Compose, go to https://github.com/docker/compose and download the release for your OS: `wget https://github.com/docker/compose/releases/download/v2.5.0/docker-compose-linux-x86_64 -O docker-compose`. The flag `-O docker-compose` assigns the name docker-compose to the downloaded file.

Make it executable: `chmod +x docker-compose`.

Add the `soft/` directory to `PATH` environment variable so that the folder is accessible from anywhere. Open the `.bashrc` file with nano: `nano ~/.bashrc`. In `.bashrc`, add the following line: `export PATH="${HOME}/soft:${PATH}"`. 

Save it and run the following command to make sure the changes are applied: `source ~/.bashrc`. To check that everything worked as expected and the file `docker-compose` is accessible, run `which docker-compose` and the displayed path should be `/home/ubuntu/soft/docker-compose`.

- Step 5: Run Docker
  - `docker run hello-world`

If you get the following error: 

    docker: Got permission denied while trying to connect to the Docker daemon socket at unix:///var/run/docker.sock: Post "http://%2Fvar%2Frun%2Fdocker.sock/v1.24/containers/create": dial unix /var/run/docker.sock: connect: permission denied. 
    
then make sure that you ran the commands at the end of `Step 3` above; then restart your VM instance.

**Note:** If you get the following error: 

    It is required that your private key files are NOT accessible by others. This private key will be ignored. 

then you should change permits on the downloaded key file to protect your private key: `chmod 400 name-of-your-private-key-file.pem`.

- Step 6: Clone the repo
  - Unless you want to push to GitHub, use `https`: `git clone https://github.com/DataTalksClub/mlops-zoomcamp.git`

- Step 7: To get access to a remote AWS instance:
  - Install the `Remote - SSH` extension and connect to the `mlops-zoomcamp` in VS Code

You can now launch a Jupyter notebook on the remote instance:
- Create the `notebooks` folder in `~/`: `mkdir notebooks`
- `jupyter notebook` 
  - Notice that we launched the Jupyter Notebook on the remote machine. Therefore, if we paste the created URL link into the local browser, it won't work
  - We need to use port forwarding to connect the remote port on the remote machine to the local port on the local machine
  - In VS Code go to `Ports`, select `Forward Port` and type in `8888`
  - You should now be able to access the Jupyter notebook launched on the remote machine from the local browser