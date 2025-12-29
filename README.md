# ROS2課題

ロボットの障害物検知および緊急停止機能をシミュレーションするROS 2パッケージです。
擬似的な距離センサーの値を監視し、一定距離（1.0m）未満になると停止信号を発行します。

![test](https://github.com/[あなたのGitHubユーザー名]/robot_safety_system/actions/workflows/test.yml/badge.svg)

## 必要環境
* Ubuntu 22.04 LTS
* ROS 2 Humble Hawksbill
* Python 3.10

## インストール方法
ワークスペースの `src` ディレクトリに移動し、リポジトリをクローンしてください。

```bash
cd ~/ros2_ws/src
git clone [https://github.com/](https://github.com/)[あなたのGitHubユーザー名]/robot_safety_system.git
```

## 実行方法
以下のコマンドで、センサーノードとブレーキノードを同時に起動します。

* ros2 launch robot_safety_system safety_system_launch.py

## 実行結果の例
以下のように、距離に応じて GO または STOP が表示されます。

[INFO] [launch]: All log files can be found below ...
[INFO] [sensor-1]: process started with pid [1234]
[INFO] [brake-2]: process started with pid [1235]
[brake-2] [INFO] [safety_brake]: Safety Brake System is ready.
[sensor-1] [INFO] [sensor_simulator]: Sensor Simulator has started.
[sensor-1] [INFO] [sensor_simulator]: Publishing distance: 2.54m
[brake-2] [INFO] [safety_brake]: Safe. Distance: 2.54m. GO.
...
[sensor-1] [INFO] [sensor_simulator]: Publishing distance: 0.85m
[brake-2] [WARN] [safety_brake]: DANGER! Distance: 0.85m. STOP!

* Ctrl+C で終了

## テスト方法
以下のコマンドで、ライセンス準拠やコードスタイルのテストを実行できます。

colcon test --packages-select robot_safety_system

## ライセンス
このソフトウェアは、Apache License 2.0の下で公開されています。 詳細についてはLICENSEファイルを確認してください。

* SPDX-FileCopyrightText: 2025 浅野真夢
* SPDX-License-Identifier: Apache-2.0

```bash
vim LICENSE
wget https://www.apache.org/licenses/LICENSE-2.0.txt -O LICENSE
```











