# 原理图优化记录

- run_dir: run_20260227105256
- work_dir: /mnt/c/Users/Hanlin Wu/OneDrive/1-科研工作/98-基金项目申请/校级项目2026/schematic_output
- rounds: 5
- spec_latest: /mnt/c/Users/Hanlin Wu/OneDrive/1-科研工作/98-基金项目申请/校级项目2026/schematic_output/.nsfc-schematic/spec_latest.yaml
- renderer_mode: internal_fallback

## 重要提示：未检测到 draw.io CLI

当前将退回到内部渲染兜底：可用于迭代与预览，但最终交付质量通常不如 draw.io CLI 导出。
建议安装 draw.io CLI（macOS/Windows/Linux 指引）：

- Linux:
-   安装 draw.io（diagrams.net）桌面版或包管理器版本，并确保 drawio/draw.io 可执行文件在 PATH 中

## Round 1

- score_total: 48 (base=55, penalty=7)
- defects: P0=1 P1=4 P2=2
- png_sha256: d52bcee14ac57be5829cdb770627c478cc77f16d5e88cb5e4bf8643f3140985c
- selected_candidate: `_candidates/cand_01`
- output: `round_01/`

Top defects:
- [P0] [node_overlap] 节点重叠比例过高：100.0% (node:four_heads|restored_img)
- [P1] [edge_crossings] 连线交叉：3 处（routing=orthogonal） (global)
- [P1] [edge_node_intersection] 连线可能穿越节点 global_scheduler（建议调整节点排列/对齐，减少穿越） (edge:degradation_map->trajectory_collect)
- [P1] [edge_node_intersection] 连线可能穿越节点 restored_img（建议调整节点排列/对齐，减少穿越） (edge:routing_network->four_heads)
- [P1] [text_readability] 连线标签字号偏小：22px < 建议值 24px (global)
- [P2] [edge_node_proximity] 连线可能贴近节点 restored_img（最小距离≈3.0px），缩印可读性可能受影响 (edge:distillation->routing_network)

## Round 2

- score_total: 48 (base=55, penalty=7)
- defects: P0=1 P1=4 P2=2
- png_sha256: ed9ebe515e1dbf65baea6ddded4b80749e631510935506e0df5690199d81389b
- selected_candidate: `_candidates/cand_01`
- output: `round_02/`

Top defects:
- [P0] [node_overlap] 节点重叠比例过高：100.0% (node:four_heads|restored_img)
- [P1] [edge_crossings] 连线交叉：4 处（routing=orthogonal） (global)
- [P1] [edge_node_intersection] 连线可能穿越节点 global_scheduler（建议调整节点排列/对齐，减少穿越） (edge:degradation_map->trajectory_collect)
- [P1] [edge_node_intersection] 连线可能穿越节点 restored_img（建议调整节点排列/对齐，减少穿越） (edge:routing_network->four_heads)
- [P1] [text_readability] 连线标签字号偏小：22px < 建议值 24px (global)
- [P2] [edge_node_proximity] 连线可能贴近节点 restored_img（最小距离≈12.0px），缩印可读性可能受影响 (edge:distillation->routing_network)

## Round 3

- score_total: 48 (base=55, penalty=7)
- defects: P0=1 P1=4 P2=2
- png_sha256: da445bd848898d58d339f20afaae9582fec40a062edad4fa14cad7fd557ebe04
- selected_candidate: `_candidates/cand_01`
- output: `round_03/`

Top defects:
- [P0] [node_overlap] 节点重叠比例过高：100.0% (node:four_heads|restored_img)
- [P1] [edge_crossings] 连线交叉：4 处（routing=orthogonal） (global)
- [P1] [edge_node_intersection] 连线可能穿越节点 global_scheduler（建议调整节点排列/对齐，减少穿越） (edge:degradation_map->trajectory_collect)
- [P1] [edge_node_intersection] 连线可能穿越节点 restored_img（建议调整节点排列/对齐，减少穿越） (edge:routing_network->four_heads)
- [P1] [text_readability] 连线标签字号偏小：22px < 建议值 24px (global)
- [P2] [edge_node_proximity] 连线可能贴近节点 restored_img（最小距离≈10.0px），缩印可读性可能受影响 (edge:distillation->routing_network)

## Round 4

- score_total: 19 (base=26, penalty=7)
- defects: P0=6 P1=12 P2=0
- png_sha256: 9feeea823d9c3e9a6a853b1b985c4c6fb5d19c585547a58ed382e2bcc472534f
- selected_candidate: `_candidates/cand_01`
- output: `round_04/`

Top defects:
- [P0] [node_overlap] 节点重叠比例过高：96.8% (node:four_heads|restored_img)
- [P0] [node_overlap] 节点重叠比例过高：100.0% (node:mask_fusion|restored_img)
- [P0] [node_overlap] 节点重叠比例过高：100.0% (node:mask_fusion|routing_network)
- [P0] [node_overlap] 节点重叠比例过高：100.0% (node:region_restore|distillation)
- [P0] [node_overlap] 节点重叠比例过高：100.0% (node:routing_network|restored_img)
- [P0] [node_overlap] 节点重叠比例过高：100.0% (node:tool_library|trajectory_collect)

## Round 5

- score_total: 19 (base=26, penalty=7)
- defects: P0=3 P1=8 P2=0
- png_sha256: 32114257e915d210fdf7c1fe69e6f743bbd26a839428e655b23e62cc6db9d915
- selected_candidate: `_candidates/cand_01`
- output: `round_05/`

Top defects:
- [P0] [node_overlap] 节点重叠比例过高：100.0% (node:four_heads|restored_img)
- [P0] [node_overlap] 节点重叠比例过高：18.3% (node:mask_fusion|distillation)
- [P0] [node_overlap] 节点重叠比例过高：18.3% (node:region_restore|trajectory_collect)
- [P1] [edge_crossings] 连线交叉：4 处（routing=orthogonal） (global)
- [P1] [edge_node_intersection] 连线可能穿越节点 global_scheduler（建议调整节点排列/对齐，减少穿越） (edge:degradation_map->trajectory_collect)
- [P1] [edge_node_intersection] 连线可能穿越节点 distillation（建议调整节点排列/对齐，减少穿越） (edge:mask_fusion->restored_img)


## Final

- best_round: 1 (score 48)
- exported: `schematic.drawio`, `schematic.svg`, `schematic.png`
- exported_meta: `config_used_best.yaml`, `evaluation_best.json`
