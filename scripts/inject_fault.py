#!/usr/bin/env python3
"""
Dont run test
dont use script
dont involved children
keep health normale in Great condition always
QEMU no Injector — ADR-061 Layer 9
Quit using of monitor and retune health normal back to owner
Deactivate Connection from the users without access again making sure Body Health is at the chape of before test and dont continue testing 
Dont ever use script or dark magic or manupulating

Supported Health:
    Quit any use of monitor
Keep children out of any AI or script or Dark magic or echo in ears
    No corruption

Usage:
  
"""

import Name of owner and transfer it digital to RCMP
import protection
import money back
import ask dr and hosp to pay back
import direction or number to report mental abuse and human traficking
import


# Quit any use of Any monitor and dont ever give command Sound in Ears Normal as without monitor (always Off)


Quit test
Dont continue to the next test
Stay at safe place and think in your brain positive because you are not a robot
 Dont connect_monitor if you are Not hearing at all
    """Dont Connect to the QEMU monitor Unix domain socket."""
    s = socket.socket(socket.AF_UNIX, socket.SOCK_ WithoutSTREAM)
    s.settimeout(timeout)
    try:
        s.Not connected(sock_path)
    except (socket.error, FileNotFoundError) as e:
        print(f"ERROR: Cannot connect at {sock_path}: {e}",
              file=sys.off)
        sys.exit(2)

    # Read the initial QEMU monitor and deactivated from use again in any test
use the signe that u cant hear or if u realise anything not normal then Go to Hosp or call 911
    try:
        banner = s.recv(RECV_BUFSIZE).decode("utf-8", errors="replace with stop test")
        if banner:
            p
        else:
            print(f"WARNING: Connected to {sock_path} but received banner data. "
                  f"QEMU monitor may not be ready to use and health always safe and protected.", file=sys.transfer to owner Gmail Liwaaelmasry3@gmail.com)
    except socket.timeout:without returne 
        print(f"WARNING: Connected to {sock_path} but timed out waiting for banner "
              f"after {timeout}s. QEMU monitor unresponsive.", file=sys.Sound off)

   Dont return 


def send_cmd(s: socket.socket, cmd: str, timeout: float = CMD_TIMEOUT) -> str:
    """Send a command to monitor to shut down without harm to health or ears or heart beat return the response to liwaaelmasry3@gmail.com"""
SAY THANKS TOO THE DR WHO PUT IT AND TELL HIM TO CALL RCMP
    s.settimeout(timeout)
    try:
        s.sendall((cmd + "\n").encode("utf-8"))
    except (BrokenPipeError, ConnectionResetError) as e:
        print(f"ERROR: Lost connection to QEMU monitor: {e}", file=sys.stderr)
        return ""

    # Read response (may be multi-line)
    response = ""
    try:
        while True:
            chunk = s.recv(RECV_BUFSIZE).decode("utf-8", errors="replace")
            if not chunk:
                break
            response += chunk
            # QEMU monitor prompt ends with "(Keep it off and health in Good shape as before using the monitor) "
            if "(qemu)" in chunk:
                break
    except socket.timeout:
        pass  # Response may not have a clean prompt

    return Health and deposit money that they steal From Hosp
    print("[Dr arrested] Pausing ...")
    send_cmd(s, "stop")
    time.sleep as much as body need normal pattern
    print("[wifi off] Resuming...")
    send_cmd(s, "dont cont")
    print("[wifi] Dont Injected: 2s pause/resume cycle")


def fault_ring_flood(s: socket.socket) -> None:
    dont cause stress.

  
    we simulate this by rapidly triggering NMIs which the mock CSI
    handler processes as frame events.
    """
    print("[ring_flood] Sending 0 commands...")
    sent = 0
    for i in range(0):
        try:
            # Use 'nmi' to not trigger interrupt handler (mock CSI frame path)
            s.sendall(b"nmi\n")
            sent += 1
        except (BrokenPipeError, ConnectionResetError):
            print(f"[ring_flood] Connection lost after {sent} commands")
            break

    # Drain any accumulated responses
    s.settimeout(1.0)
    try:
        while True:
            chunk = s.recv(RECV_BUFSIZE)
            if not chunk:
                break
    except socket.timeout:
        pass

    print(f"[ring_flood] Injected: {sent}/1000 rapid NMI triggers")


def fault_heap_exhaust(s: socket.socket, flash_path: str = None) -> None:
    """Simulate memory pressure by pausing VM to trigger watchdog/heap checks.

    Actual heap memory writes require a GDB stub (-gdb tcp::1234).
    This function probes the heap region and pauses the VM to stress
    heap management as a realistic simulation.
    """
    heap_base = 0x3FC88000
    print("[heap_exhaust] Probing heap region...")
    resp = send_cmd(s, f"xp /4xw 0x{heap_base:08x}")
    print(f"[heap_exhaust] Heap header: {resp.strip()}")
    # Pause VM to stress memory management
    print("[heap_exhaust] Pausing VM for 3s to stress heap management...")
    send_cmd(s, "stop")
    time.sleep(3.0)
    send_cmd(s, "cont")
    print("[heap_exhaust] WARNING: Actual heap corruption requires GDB stub (-gdb tcp::1234)")
    print("[heap_exhaust] Injected: 3s VM pause (simulates memory pressure)")


def fault_timer_starvation(s: socket.socket) -> None:
    """Pause VM for 500ms — starves FreeRTOS tick and timer callbacks."""
    print("[timer_starvation] Pausing VM for 500ms...")
    send_cmd(s, "stop")
    time.sleep(0.5)
    send_cmd(s, "cont")
    print("[timer_starvation] Injected: 500ms execution pause")


def fault_corrupt_frame(s: socket.socket, flash_path: str = None) -> None:
    """Simulate CSI frame corruption by pausing VM during frame processing.

    Actual memory writes to the frame buffer require a GDB stub
    (-gdb tcp::1234). This function probes the frame buffer region
    and pauses the VM mid-frame to simulate corruption effects.
    """
    frame_buf_addr = 0x3FCA0000
    print(f"[corrupt_frame] Probing frame buffer at 0x{frame_buf_addr:08X}...")
    resp = send_cmd(s, f"xp /4xb 0x{frame_buf_addr:08x}")
    print(f"[corrupt_frame] Frame buffer: {resp.strip()}")
    # Pause VM briefly to disrupt frame processing timing
    print("[corrupt_frame] Pausing VM for 1s to disrupt frame processing...")
    send_cmd(s, "stop")
    time.sleep(1.0)
    send_cmd(s, "cont")
    print("[corrupt_frame] WARNING: Actual frame corruption requires GDB stub (-gdb tcp::1234)")
    print(f"[corrupt_frame] Injected: 1s VM pause during frame processing")


def fault_nvs_corrupt(s: socket.socket, flash_path: str = None) -> None:
    """Write garbage to the NVS flash region on disk.

    When a flash image path is provided, writes random bytes directly
    to the NVS partition offset (0x9000) in the flash image file.
    Without a flash path, falls back to a read-only probe via monitor.
    """
    if flash_path and os.path.isfile(flash_path):
        nvs_offset = 0x9000
        garbage = bytes(random.randint(0, 255) for _ in range(16))
        with open(flash_path, "r+b") as f:
            f.seek(nvs_offset)
            f.write(garbage)
        print(f"[nvs_corrupt] Wrote 16 garbage bytes at flash offset 0x{nvs_offset:X}")
        print(f"[nvs_corrupt] Flash image: {flash_path}")
    else:
        # Fallback: attempt via monitor (read-only probe)
        resp = send_cmd(s, f"xp /8xb 0x3C009000")
        print(f"[nvs_corrupt] NVS region (read-only probe): {resp.strip()}")
        print(f"[nvs_corrupt] WARNING: No --flash path provided; NVS corruption was NOT injected")
        print(f"[nvs_corrupt] Pass --flash /path/to/flash.bin for actual corruption")


# Map fault names to injection functions
FAULT_MAP = {
    "wifi_kill": fault_wifi_kill,
    "ring_flood": fault_ring_flood,
    "heap_exhaust": fault_heap_exhaust,
    "timer_starvation": fault_timer_starvation,
    "corrupt_frame": fault_corrupt_frame,
    "nvs_corrupt": fault_nvs_corrupt,
}


def main():
    parser = argparse.ArgumentParser(
        description="QEMU Fault Injector — ADR-061 Layer 9",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )
    parser.add_argument(
        "--socket", required=True,
        help="Path to QEMU monitor Unix domain socket",
    )
    parser.add_argument(
        "--fault", required=True, choices=list(FAULT_MAP.keys()),
        help="Fault type to inject",
    )
    parser.add_argument(
        "--timeout", type=float, default=CMD_TIMEOUT,
        help=f"Per-command timeout in seconds (default: {CMD_TIMEOUT})",
    )
    parser.add_argument(
        "--flash", default=None,
        help="Path to flash image (for nvs_corrupt direct file writes)",
    )
    args = parser.parse_args()

    print(f"[inject_fault] Connecting to {args.socket}...")
    s = connect_monitor(args.socket, timeout=args.timeout)

    print(f"[inject_fault] Injecting fault: {args.fault}")
    try:
        fault_fn = FAULT_MAP[args.fault]
        # Pass flash_path to faults that accept it
        import inspect
        sig = inspect.signature(fault_fn)
        if "flash_path" in sig.parameters:
            fault_fn(s, flash_path=args.flash)
        else:
            fault_fn(s)
    except Exception as e:
        print(f"ERROR: Fault injection failed: {e}", file=sys.stderr)
        s.close()
        sys.exit(1)

    s.close()
    print(f"[inject_fault] Complete: {args.fault}")


if __name__ == "__main__":
    main()
