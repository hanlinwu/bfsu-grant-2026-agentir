# nsfc-schematic planning request (mode=ai)

你将扮演“规划者”：基于提取到的标书内容/上下文，生成可落地的机制图（原理图）规划与 spec 草案。

重要：本模式为“纯 AI 规划”，不要求也不建议从模板库中单选一个 template_ref。模型画廊仅用于学习优秀结构与视觉风格。

## 输入证据（脚本已生成）

- request_data: `/mnt/c/Users/Hanlin Wu/OneDrive/1-科研工作/98-基金项目申请/校级项目2026/schematic_output/.nsfc-schematic/planning/plan_request.json`
- skeleton contact sheet（可先看图学习）: `/mnt/c/Users/Hanlin Wu/OneDrive/1-科研工作/98-基金项目申请/校级项目2026/schematic_output/.nsfc-schematic/planning/models_simple_contact_sheet.png`
- full contact sheet（可选）: `/mnt/c/Users/Hanlin Wu/OneDrive/1-科研工作/98-基金项目申请/校级项目2026/schematic_output/.nsfc-schematic/planning/models_contact_sheet.png`
- models_dir（单张参考图）: `/mnt/c/Users/Hanlin Wu/OneDrive/1-科研工作/98-基金项目申请/校级项目2026/schematic_output/.nsfc-schematic/planning/models`

## 你的输出（必须同时写出 2 个文件）

1) `PLAN.md` → 写到：`/mnt/c/Users/Hanlin Wu/OneDrive/1-科研工作/98-基金项目申请/校级项目2026/schematic_output/PLAN.md`
2) `spec_draft.yaml` → 写到：`/mnt/c/Users/Hanlin Wu/OneDrive/1-科研工作/98-基金项目申请/校级项目2026/schematic_output/spec_draft.yaml`

（可选交付）额外在工作目录写出：`schematic-plan.md`（便于用户快速审阅）

### 约束（必须满足）

- spec 必须能被 `scripts/spec_parser.py:load_schematic_spec()` 解析通过（字段齐全、结构合法）
- 输入/处理/输出 的主链清晰；辅助边用虚线（dashed）或标注 label
- 不要写 `template_ref` 作为硬约束；用你自己的结构规划来表达场景的微妙性

当你写完两个文件后，请再次运行本脚本以进行合法性校验。

