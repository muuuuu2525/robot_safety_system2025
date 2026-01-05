#!/bin/bash
# SPDX-FileCopyrightText: 2025 Taro Chiba
# SPDX-License-Identifier: Apache-2.0

dir=~
[ "$1" != "" ] && dir="$1"

cd $dir/ros2_ws
colcon build --symlink-install
source install/setup.bash

# ノードを10秒間だけ起動して、出力をログファイルに保存
timeout 10 ros2 launch robot_safety_system safety_system_launch.py > /tmp/robot_safety.log

# ログファイルの中身をチェック
cat /tmp/robot_safety.log | grep 'Publishing distance:'
if [ $? -ne 0 ]; then
    echo "Test Failed: Sensor data not found"
    exit 1
fi

cat /tmp/robot_safety.log | grep 'safety_brake'
if [ $? -ne 0 ]; then
    echo "Test Failed: Brake node output not found"
    exit 1
fi

echo "Test Passed: All expected outputs found."
