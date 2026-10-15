# 2026-10-15 六小时快照原始结果

本目录归档用户提供的两份原始ZIP及其全部解压JSON，文件内容保持原样。

| 算例 | 机队 | 快照 | 最好 Tmax/h | 状态 |
|---|---:|---|---:|---|
| Case1 | 3 | [快照文件](snapshot_1792064931712292139/) / [原始ZIP](snapshot_1792064931712292139.zip) | 10.247496253716081 | UNKNOWN |
| Case3 | 4 | [快照文件](snapshot_1792064928918013842/) / [原始ZIP](snapshot_1792064928918013842.zip) | 9.403611015410183 | UNKNOWN |

两份ZIP的CRC检查通过；Case1的19份、Case3的7份求解档案均通过独立校验。检查覆盖任务副本完整性、路线数量、非空路线、禁止相邻同物理点、闭合飞行时间、服务时间、输入指纹和状态一致性。物理点导出逐路线核对通过；run.json中的求解器源码SHA256与提交36bd8b0一致。

校验通过不表示九小时可行，也不表示最优。浮点独立复算可能产生约1e-15小时的末位差异。没有新增运行或重新执行六小时搜索。

- [校验记录](validation.json)
- [原始文件SHA256清单](manifest.json)
- [完整报告与后续计划](../../SIX_HOUR_REPORT_20261015.md)

`best.json`可用于内部任务副本格式热启动；`best_physical.json`便于查看物理点路线，不能直接作热启动输入。检查点只代表快照时刻，不能恢复此前全部轮次的历史。

`validate_snapshot.py`逐字复制自提交`36bd8b0d9c4bc0a8e846c0cb965bc6eb29352cee`的`research/alns_next/validate.py`。在本目录执行：

```bash
python3 validate_snapshot.py snapshot_1792064931712292139/best.json --data ../../instances.json
python3 validate_snapshot.py snapshot_1792064928918013842/best.json --data ../../instances.json
```
