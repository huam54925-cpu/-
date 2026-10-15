# 固定机队 ALNS 后续研究原型

针对论文问题一的后续改进：以 Case1 固定三架突破 10.3195 小时为主要研究目标，最终仍按每条路线不超过 9 小时验收。

实现四类破坏、贪心/regret-2 修复、自适应算子权重，以及 2-opt、2-opt* 和长度 2～3 的 Or-opt。分别保存最好最长时间、最低总超时量及九小时内可行解。独立验证器从坐标重算距离、时间与任务覆盖。

## 运行

仅需 Python 3 标准库。在本目录执行：

```bash
python3 alns_solver.py --case Case1 --fleet 3 --seconds 60 --seed 0 --out case1.json
python3 validate.py case1.json
python3 -m unittest -v test_solver.py
```

使用 `--focus violation` 增强超时惩罚，使用 `--warm case1.json` 从此前最好时间路线重新开始。检查点支持热启动，尚不支持随机数与退火状态的精确恢复。

## 当前验证结果

25 秒短测完成 345 轮，Case1 三架从初始 11.20696 小时降至 10.43347 小时。独立结构与时间校验通过，3 项自动测试通过。仍未达到九小时，也未突破论文的 10.3195 小时；输出状态为 `UNKNOWN`，不能据此判断三架不可行。

这里没有运行六小时正式实验，也没有建立优于旧算法的公平对照结论。Cross-exchange、Ejection chain、遗传算法及岛模型尚未实现。

输入来自源仓库提交 `f4f6ece1cbc21831512211ff25a6e971e59d860d` 的附件1，转换数据及源表哈希见 `instances.json`。

详细算法、参数、验证结果和正式实验建议见 [算法设计与运行说明](算法设计与运行说明.txt)。原论文程序保留在 `submission_package/`。
