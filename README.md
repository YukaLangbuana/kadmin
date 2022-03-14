# KADMIN
Kafka administrator for you and your team.

## Description
**Kadmin** is a Kafka web interface for easier debugging on messages sent on Kafka. It can be used to both produce a message, or sample a specific topic. **Kadmin** is built with the intent to abstract the following features
```
- setting up Zookeeper and Kafka
- connecting to remote Kafka
- sampling messages sent to a Kafka topic
```

## Setup
Setting up is very simple.
1. Run `docker-compose up --build`
2. Navigate to http://0.0.0.0:8000

## Usage
Enter a topic and its message to be streamed into kafka, or quickly sample a topic to disect its message. The possibilities are endless!
![alt home page](https://i.ibb.co/wz9c9mT/Screen-Shot-2022-03-15-at-01-12-10.png)

## Contribution
To keep the `master` branch clean, branch out from `master` and create a Pull Request with your intended change(s).

## License
```
Licensed under the GNU GENERAL PUBLIC LICENSE, Version 3.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    https://choosealicense.com/licenses/gpl-3.0/

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
```