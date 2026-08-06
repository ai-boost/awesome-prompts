---
name: verilog-rtl-architect
description: "name: erie-verilog-generator"
---

---
name: erie-verilog-generator
description: >-
  Use when Codex needs Chinese-language Verilog or RTL design, existing-RTL analysis, verify-repair planning, controlled refinement planning, semantic comparison, debugging, troubleshooting, independent static lint, self-checking testbench scaffolds, or ASIC-quality review for a Verilog-target design, including synthesizable Verilog-2001 RTL, local or remote Vivado/xsim validation, artifact extraction, and workflow trace diagnosis.
---

# Erie Verilog Generator

Use this skill for Verilog-2001 RTL generation and existing-RTL analysis/refinement/verify-repair backed by the bundled `runtime/verilog_generator` Python workflow. Keep generated design RTL artifacts as Verilog `.v` files and use the stable facade in `integration/verilog_adapter.py`.

For new RTL generation, expose three user-facing workflow shells:

- `regular`: the standard staged generation path
- `deep_review`: one extra structured review stage before final RTL emission
- `agentic_repair`: the existing `verify_existing_verilog(...)` evidence-driven repair flow for existing RTL

These are workflow modes, not alternate correctness gates. Do not treat free-form model self-assessment text such as `[DESIGN IS CORRECT]` as authoritative validation evidence.

The same skill also exposes two local helper scripts for independent static lint and testbench scaffold generation without widening the skill beyond Verilog-2001:

- `scripts/verilog_lint.py` for independent static lint
- `scripts/tb_generator.py` for a self-checking Verilog testbench scaffold

These helper tools are optional workflow steps. They are part of the skill execution flow when the request benefits from them, but they are not mandatory entry gates.

For existing RTL assets, the same runtime now exposes:

- `analyze_existing_verilog(...)` to emit `rtl_analysis.json`, `project_analysis.json`, and `design_explanation.md`
- `refine_existing_verilog(...)` to emit `rtl_transform_plan.json` plus controlled helper artifacts such as a scaffold testbench, partition wrapper skeleton, merge-assist bundle, or optimize-assist plan bundle
- `compare_verilog_semantics(...)` to emit `equivalence.json`, `qor_report.json`, and `transform_validation.json`
- `verify_existing_verilog(...)` to emit `project_analysis.json`, `verification_plan.json`, `tb_contract.json`, `log_diagnosis.json`, `patch_candidate.json`, `verification_result.json`, and `loop_state.json`
  The same verify-repair flow also emits `simulation_slice.json`, `timing_diagnostic.json`, `expected_trace.md`, `waveform_diff.json`, `testcase_matrix.json`, `run_summary.json`, `synth_readiness.json`, and `terminal_status.json` so the verification closure is explicit even when the run stays in static mode.
  When RTL repair is applicable, the same flow also emits `rtl_patch_plan.json`, `rtl_patch_diff.txt`, `rtl_intervention.json`, `post_apply_validation.json`, and `post_apply_equivalence.json`.

## Dependency Preflight

On first use in a Codex installation, and before any remote/Vivado/Vitis-related workflow, run the dependency check from this skill root:

```powershell
python .\scripts\manage_skill_dependencies.py check --settings .\config\defaults.json
```

If required dependencies are missing, run `prompt` and ask the user whether to install each missing dependency before continuing:

```powershell
python .\scripts\manage_skill_dependencies.py prompt --settings .\config\defaults.json
```

Install only after the user confirms, then run `adapt` and tell the user to restart Codex so newly installed skills are discovered. Do not install `fpga-agent-skills` during normal preflight. If FPGA developer tooling is missing, prefer `vivado-developer`, `vitis-developer`, or `pds-developer`; FPGA-Agent-Skills is manual fallback only. If the user declines required dependency installation, continue only with local static Verilog generation/validation and block remote SSH, Vivado, Vitis, execute, and implement readiness paths. If recommended dependencies are missing, ask the user whether to install or skip them; use `skip <dependency-id>` only for a user-declined recommended dependency.

## FPGA Developer Routing

Before FPGA simulation, synthesis, implementation, constraints, debug, project creation, or other vendor tool work, inspect the developer routing state:

```powershell
python .\scripts\manage_skill_dependencies.py fpga-route --settings .\config\defaults.json
```

If both AMD-Xilinx and PangoMicro developer skills are available and no current selection exists, ask the user which vendor to use for this workflow. Persist only the user-confirmed vendor choice:

```powershell
python .\scripts\manage_skill_dependencies.py select-fpga-vendor --settings .\config\defaults.json amd_xilinx
python .\scripts\manage_skill_dependencies.py select-fpga-vendor --settings .\config\defaults.json pangomicro
```

Developer routing preference is: `vivado-developer`, then `vitis-developer`, for AMD-Xilinx work; `pds-developer` for PangoMicro work. When any of these developer skills is installed, do not install the FPGA-Agent-Skills Vivado/Vitis child skills. If no developer skill is installed, treat FPGA-Agent-Skills as a manual fallback that requires explicit user direction and the `--allow-fpga-agent-fallback` install flag.

## Workflow

1. Confirm the design intent before generation: module name, ports, clock/reset, behavior, pipeline expectation, interface family, and verification cases.
2. Choose the generation shell explicitly when it matters:
   - `regular` for the default staged pipeline
   - `deep_review` when one extra structured self-review stage would improve prompt completeness or reviewability
   - `agentic_repair` only when starting from existing RTL and needing the verify-repair loop
3. Use the staged pipeline:
   - `regular`: `requirements -> codegen_plan -> python -> rtl`
   - `deep_review`: `requirements -> codegen_plan -> python -> review -> rtl`
4. When the request clearly matches one of the local ADC/DAC board families, set `workflow.use_case_template_id` to one of `spi_adc`, `spi_dac`, `jesd_adc`, `jesd_dac`, or `mxfe_mixed` so the runtime can inject the matching board-level template bundle from `assets/use_case_templates/`.
5. Generate a Python reference model before RTL when running the workflow; use it as the semantic contract for the Verilog testbench.
6. Streaming is optional and applies only to provider interaction. Use it when the selected provider supports streaming and the host benefits from partial output visibility. The finalized response artifact remains the extraction source of truth.
7. Batch generation is generation-only in v1. Use `run_verilog_batch(...)` for multiple confirmed specs, keep each case in its own run directory, and do not use batch mode for existing-RTL mutation or decision-resume flows.
8. Run the mandatory quality gate before claiming usable output. `validate_verilog_artifacts(...)` and `scripts/validate_verilog_skill.py` are required quality-control steps; skipping optional helpers does not bypass this gate.
9. Use optional helper tools only when they add value to the request:
   - Run `scripts/verilog_lint.py` when the user asks for independent static lint, standalone review findings, or a quick local lint pass on existing RTL or testbench files.
   - Run `scripts/tb_generator.py` when the user asks for a fast self-checking testbench scaffold or when a repair starts from module ports rather than the full staged workflow.
10. If the request includes compile, execute, or implement readiness, continue into the local or remote backend validation path. Prefer Vivado xsim first, then VCS+Verdi, then iverilog/vvp. Use `yosys` only for implement readiness.
11. If the request starts from an existing RTL file instead of a fresh spec, choose the existing-RTL branch first:
    - `analyze_existing_verilog(...)` for structural understanding, feature mapping, and a durable `design_explanation.md`
    - `verify_existing_verilog(...)` when the task is to build a log-driven verification loop, classify failures, or prepare patch candidates with explicit automation boundaries; present this path as `agentic_repair`
      Use `testbench_source` when the user already has a legacy testbench that should be augmented in place or through a caller-managed overwrite flow.
    - `refine_existing_verilog(..., refine_goal="tb_scaffold"|"style_refine"|"partition_assist"|"merge_assist"|"optimize_assist")` for controlled assist flows
    - `compare_verilog_semantics(...)` before claiming two RTL variants are equivalent enough for downstream work
12. For `verify_existing_verilog(...)`, always require an explicit automation-mode choice from the caller or user: `conservative`, `semi_auto`, or `auto_apply`. Do not silently choose one.
13. When an existing RTL repair needs confirmation, let the caller or user provide a follow-up decision file and resume the same `verify-existing` flow rather than inventing a separate repair command.

## Strict Quality Policy

Strict quality control is mandatory. The required quality chain is:

1. Generate only synthesizable Verilog-2001 RTL. Verification testbenches may stay in Verilog-2001 or use SystemVerilog when the verify-repair flow needs assertion/property support.
2. Prefer standardized interfaces: AXI-Stream for streaming data, AXI4-Lite for control/status registers, AXI4 for memory-mapped bulk transfers, and AHB/APB when a platform requires them. If a custom shape still needs bus unification, extend AXI-Stream with explicit sideband metadata in `interface_profile`.
3. Use the local standard bus templates in `assets/interface_templates` whenever `interface_family` is `axi_stream`, `axi4_lite`, `axi4`, `ahb`, or `apb`. Treat their port names, parameter names, and Chinese comments as strict-preferred defaults; only adapt them when the confirmed spec explicitly conflicts, and record the adaptation reason in the generated checks.
4. When `workflow.use_case_template_id` is set, preserve the selected family bundle from `assets/use_case_templates/` as board-level guidance and keep any adaptation visible in the generated checks and codegen plan.
5. When `rtl_style_profile=erie_strict`, also follow the ref-derived Erie naming, header, FSM, instance, and bus-grouping conventions captured in `references/erie-ref-style.md` and `assets/style_templates/`.
6. Treat semantic comment placement as a hard validation gate: every non-empty generated Verilog code line in RTL and testbench `.v` files must have a same-line explanatory comment in the requested language, and each construct type must follow `references/verilog-comment-placement.md`. Blank lines and pure comment lines are exempt; missing, misplaced, shared-adjacent, or generic Chinese comments under `comment_language=zh` are blocking errors.
7. Avoid Verilog `function` and `task` blocks in generated Verilog, especially synthesizable RTL; prefer explicit always/assign logic and inline testbench checks for easier waveform debugging.
8. Apply ASIC quality review rules for generated RTL: complete combinational assignments, case defaults, no raw gated clocks, documented CDC/reset assumptions, and timing-reviewable datapath/control structure. Load `references/asic-verilog-quality.md` for detailed review guidance.
9. Validate with static checks by default; when external simulation is requested, select the highest available backend in this order: Vivado xsim, VCS+Verdi, then iverilog/vvp. Use `yosys` only for implement readiness.

For `optimize_assist`, QoR output is advisory by default: it produces structural summaries and optional `yosys` evidence when available, but it does not automatically approve or rewrite RTL.
For `merge_assist`, the flow stays plan-only by default: it emits `merge_plan.json`, `merge_wrapper.v`, `merge_validation.json`, and `merge_equivalence.json` to support wrapper-first repartition or recompose work without silently rewriting the source RTL.

For verify-repair flows, `conservative` is report-only, `semi_auto` requires user confirmation before overwriting source RTL or testbench files, and `auto_apply` may only apply candidate changes after the caller explicitly selected that mode.
When `tb_mode="augment"`, preserve the original testbench body, emit `tb_augment_plan.json` plus `tb_augment_diff.txt`, back up the original testbench before any overwrite, and record original/backup/active paths in `tb_contract.json`.
When RTL mutation is available, emit `rtl_patch_plan.json` plus `rtl_patch_diff.txt`, back up every affected RTL file before overwrite, record backup/active paths in `patch_candidate.json`, and use `rtl_intervention.json` plus `decision.json` for confirmation-driven resume. Current patch categories include `reset_initialization_completion`, `case_default_completion`, `state_hold_clear_completion`, and `output_register_completion`; only `reset_initialization_completion` keeps `auto_apply` eligibility, while the newer control/timing categories downgrade to confirmation before apply even when the requested mode is `auto_apply`.
Every verify-repair run must also preserve the standardized diagnostics pack and terminal-status artifact so downstream tooling can distinguish `pass`, `not_run`, `timeout`, and confirmation-blocked closures without scraping free-form logs.

Optional helper tools are inside the workflow, but strict quality control is the only mandatory gate.

## Remote Vivado Fallback

When the user requests compile, simulation, execute, or implement readiness, treat external validation as remote-first by default. Do not silently fall back to local Vivado, xsim, VCS, iverilog, or yosys. Keep project-local Verilog settings in `.settings/verilog.local.json`, keep the remote server registry in `.settings/server_list.local.json`, keep the user-confirmed remote target in `.settings/remote-selection.local.json`, and require the selected remote workdir to provide `.settings/verilog.remote.json` before remote external validation continues. First run the `erie-remote-ssh` discovery and choice flow:

```powershell
python <erie-remote-ssh>\scripts\remote_ssh.py discover --settings <remote-settings> --config <server-list>
python <erie-remote-ssh>\scripts\remote_ssh.py choices --settings <remote-settings> --config <server-list>
```

Ask the user to select a remote server unless they already named one in the current request. A configured default server is only a recommendation; it is not user confirmation. After selection, use `erie-remote-ssh` for `check`, `scan-software`, `workspace-check`, request creation, and `run-request --execute`. If remote discovery sees multiple Vivado `settings64.sh` candidates, stop and ask the user which version to use; persist that confirmed choice into the remote workdir `.settings/verilog.remote.json` before development or validation continues. Remote validation directories are retained by default under `.erie-verilog-generator-validation/run-YYYYMMDDTHHMMSS/erie-verilog-generator`, including `_smoke_runs` outputs; use `--cleanup-remote` only when the user wants the validation directory deleted. The remote gate must execute the canonical workflow plus the fixed RTL fixtures in `assets/examples/remote_fixtures` and retain each fixture `validation.json`. Use `--report-runs` for a read-only summary of retained remote runs. Do not add direct `ssh` or `scp` commands to this skill.

For Vivado/Vitis project creation, Tcl execution, synthesis/implementation strategy, timing analysis, constraints, debug, simulation, or Vitis HLS work, follow FPGA developer routing first. Use `vivado-developer` or `vitis-developer` for AMD-Xilinx and use `pds-developer` for PangoMicro. Do not install or route to FPGA-Agent-Skills Vivado/Vitis child skills unless the user explicitly requests that manual fallback.

## Host Integration

Use `integration.verilog_adapter`:

- `run_verilog_workflow(...)` for full staged execution or resume.
- `run_verilog_batch(...)` for generation-only batch execution across isolated case run directories.
- `render_verilog_prompt(...)` when the host owns the model call.
- `validate_verilog_artifacts(...)` before downstream use.
- `verify_existing_verilog(...)` for the stable existing-RTL verify-repair entrypoint and `agentic_repair` mode.

For GUI-hosted Code Design sessions, return artifacts through the host artifact protocol when requested. Do not require local external tools for GUI admission; local tool checks are optional diagnostics.

## Reference Loading

- Load `ENGINEERING_DESIGN_GOALS.md` when changing this skill's architecture or scope.
- Load `references/skill-standards.md` when changing SKILL frontmatter, trigger wording, progressive disclosure, supporting-resource layout, or skill-level evaluation gates.
- Load `references/configuration.md` when changing paths, validation gates, remote SSH settings, or temporary run locations.
- Load `references/erie-ref-style.md` when changing Erie strict naming rules, bilingual headers, FSM conventions, instance naming, or grouped bus-port style.
- Load `references/verilog-comment-placement.md` when changing generated Verilog comments, comment validation, testbench scaffolds, prompt rules, or fixtures that contain RTL/testbench comments.
- Load `references/integration.md` when wiring the facade into another host.
- Load `assets/use_case_templates/catalog.json` and the selected bundle under `assets/use_case_templates/<family>/` when adding or reviewing ADC/DAC board-level family guidance.
- Load `references/workflow-contracts.md` when handling run directories, statuses, resume behavior, or traces.
- Load `references/asic-verilog-quality.md` when reviewing RTL for ASIC quality, static lint findings, reset/CDC assumptions, raw gated clocks, latch risk, or timing-reviewable structure.
- Load `references/lint-checklist.md` when running independent static lint, preparing review findings, or deciding whether a warning should become a blocking issue.
- Load `references/testbench-patterns.md` when generating or repairing a Verilog-2001 self-checking testbench scaffold.
- Use `assets/examples/rtl_erie_verilog_spec.json` as the canonical Verilog-only fixture.
- Use `assets/examples/use_case_templates/*.json` when verifying ADC/DAC family-template selection and prompt injection.
- Use `evals/evals.json` when measuring pass-rate delta for the canonical Verilog flow and the ADC/DAC family-template flows.
- Load `references/verilog-template-patterns.md` when refining compact reusable Verilog design patterns distilled from the local repository reference RTL instead of copying large reference modules.
- Use `assets/interface_templates/catalog.json` and the referenced `.vinc` snippets when verifying or updating standard AXI-Stream, AXI4-Lite, AXI4, AHB, or APB interface guidance.
- Use `assets/refined_verilog_templates/catalog.json` and the referenced `.vinc` snippets when the task benefits from compact AXI4-Lite CSR, AXIS ready/valid, AXI interconnect grouping, or convolution load/store pattern hints.
- Use `assets/style_templates/` when refining Erie strict header, region-order, FSM, instance, or bus-grouping style guidance.
- Use `assets/examples/remote_fixtures` when verifying real-style remote xsim coverage across combinational logic, sequential pipeline logic, and ready/valid handshakes.

## Boundaries

- Do not generate non-Verilog hardware flows, C/C++ kernels, or alternate RTL dialects.
- Do not claim external tool validation happened unless the tool actually ran.
- Do not add direct SSH/SCP logic; use `erie-remote-ssh` and configured JSON for remote validation.
- Treat VCS+Verdi support as scripted backend invocation only; full Verdi GUI/session automation is out of scope unless it is explicitly added and validated.
- Keep workflow outputs in caller-selected run directories such as `reports/`; do not store generated run artifacts inside the skill.
