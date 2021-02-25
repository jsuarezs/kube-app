# kube-app
Author: Javier Suárez (Mentoring from @pmoncadaisla)

GCP project ID: containers-project-304717

email: javisugcp@gmail.com

--
## kube-app description

Deploying simple flask counter using Redis as database.

Web flask application will receive traffic and stores/retrieves data in/from Redis so we need to deploy the application based in Python to retrieve the counter data from Redis database.

When the application is ready you will see the counter increasing with a message.

<img src = https://github.com/jsuarezs/kube-app/blob/main/images/app.png weidth = 100 height = 400>

--

### Run application locally

* Comment this line as follows in the application side in app.py: ````#start_http_server(8000)````, this is just for prometheus as client in Kubernetes deployment.
* Run ````docker-compose up```` and go to http://localhost:5000.
* Enjoy!
  

--

### Run application in Kubernetes
To test the application in Kubernetes:

* Create a flask namespace running ````kubectl create ns flask```` to create a namespace.
* Run ````kubectl apply -f k8s/ -flask -n flask```` to deploy all resources needed.
* Check NGINX ingress controller to access the app in the URL: flask.keepcoding.35-203-139-35.nip.io
* Enjoy!
* You can also check the same app deployment by HELM.
  * To deploy the app by HELM run ````kubectl create ns flask-helmns```` to create a namespace.
  * Change the context running ````kubectl config set-context --current --namespace=flask-helmns````.
  * Enter in flaskchart directory running ````cd flaskchart````.
  * Run ````helm install test . -f host.yaml```` to deploy all resources needed.
  * Access the ingress in the URL: helm.keepcoding.35-203-139-35.nip.io
  * Enjoy!

--

### Monitoring with Grafana using Prometheus engine

To deploy monitoring tools in this case Prometheus engine is getting useful data to show in Grafana dashboards.

* To deploy it you should run ````kubectl create ns monitoring```` to create a monitoring namespace.
* Enter in prometheus directory running ````cd prometheus````.
* Run ````kubectl apply -f prometheus/ -n monitoring````
* Run ````kubectl apply -f node-exporter/ -n monitoring````.
* Run ````kubectl apply -f kube-state-metrics/ -n monitoring````.
* Run ````kubectl apply -f grafana/ -n monitoring````.
* An ingress is generated and you can enter in Grafana in the URL: grafana.keepcoding.35-203-139-35.nip.io (admin/admin).


<img src = https://github.com/jsuarezs/kube-app/blob/main/images/grafana.png weidth = 100 height = 400>




--

### Monitor Networking traffic using Istio

To deploy Istio it's possible to use the Beta approach by GKE, editing the GKE cluser and enable Istio in Google Cloud Console.

* Download Istio runnig ````curl -L https://istio.io/downloadIstio | sh -````.
* Enter in Istio directory running ````cd istio-1.9.0````.
* Run ````kubectl apply -f samples/addons/kiali.yaml```` to install Kiali dashboard.
* Enter in Kiali dashboard running ````istioctl dashboard kiali````.


<img src = https://github.com/jsuarezs/kube-app/blob/main/images/istio.png weidth = 100 height = 400>