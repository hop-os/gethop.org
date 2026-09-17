# Release-day TODO — 7 September 2026

- [ ] **Remove temporary website wording before release:** review every public page for placeholders, investigation updates and superseded failure notices. Replace these with the verified release capabilities and actual remaining limitations. LicheeRV sharing and FLIP must reflect the completed framework tests (HopOS L53–L55), not an earlier debugging snapshot. Keep investigation history in the logbook. Cross-check the final website against the documentation and signed-off release evidence (L56).

- [x] **LicheeRV framework:** startup OOM fixed; four FLIPs preserve the resident and one continuous TCP socket; double FLIP reuses the original window and the full three-app workload fits afterward. Candidate hashes and scope are recorded in HopOS logbook L53.
- [x] **LicheeRV application integration:** Derek confirms Stulp works correctly with no observed regression after the ordered L59 deployment (HopOS L60). Stulp uses the configured 10.100.0.2 with unchanged job definitions; this records operator acceptance of that setup.
- [ ] **M4 write throughput:** reproduce the approximately 4000 MB/s result, record the workload and cache/flush conditions, and replace the developer-reported wording in `hopos/index.html` and the measurements documentation with the verified result.

The canonical acceptance steps and evidence live in HopOS: [release plan](../hop-os/docs/v1/technical/release-afronding.md) and [logbook](../hop-os/docs/v1/technical/release-logboek.md), entry L46. Complete these follow-ups before final publication wording is signed off. Physical network IRQ remains a later task.

- [x] **Artifact idle tracking:** a false timeout on continuously slow downloads is reproduced and fixed in HOP; slow/silent hardware fixtures and normal download repetitions pass (HopOS L54–L55). The original isolated stall did not recur; its cause is not claimed.
- [ ] **Publish transport fix:** commit/tag the HOP change, update HopOS to the actual published dependency and verify the release build. The hardware test used an isolated local replacement.

- [x] **O6N bring-up:** Derek confirms boot and full operation on 17 September 2026 (HopOS L74). O6N is listed on the hardware page. Recorded release-image lifecycle/FLIP, NVMe and duration measurements remain in the canonical release plan.
