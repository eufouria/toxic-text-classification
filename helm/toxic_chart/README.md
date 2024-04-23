# toxic-text-classifier

```shell
cd toxic_chart
helm upgrade --install classify-toxic-text .
kubectl port-forward svc/classify-toxic-text 8081:30001
```