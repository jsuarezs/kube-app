# kube-app
Author: Javier Suárez (Mentoring from @pmoncadaisla)

--
## kube-app description

Deploying simple flask counter using Redis as database.

Web flask application will receive traffic and stores/retrieves data in/from Redis.

<img src = https://github.com/jsuarezs/kube-app/blob/main/images/app.png weidth = 50 height = 100>








### Run application locally

* Comment this line as follows: ````#start_http_server(8000)````, this is just for prometheus as client in Kubernetes deployment.
* Run ````docker-compose up```` and go to http://localhost:5000.
* Enjoy!
  

--

### Run application in Kubernetes


flask.keepcoding.35-203-139-35.nip.io
helm.keepcoding.35-203-139-35.nip.io

--

### Monitoring with Grafana using Prometheus engine


grafana

grafana.keepcoding.35-203-139-35.nip.io

![Grafana](https://storage.cloud.google.com/kube-images/Captura%20de%20pantalla%202021-02-16%20a%20las%2023.49.05.png)

--

### Monitoring networking traffic using Istio

enable istio from gcp cluster gke
download istio
curl -L https://istio.io/downloadIstio | sh -
cd istio-1.9.0

run istioctl dashboard kiali

istio

![ ](https://storage.cloud.google.com/kube-images/Captura%20de%20pantalla%202021-02-17%20a%20las%2015.48.24.png)