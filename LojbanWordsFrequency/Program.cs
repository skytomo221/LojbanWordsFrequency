using System.IO;
using System.Linq;

namespace MeltywordsProject
{
    class Program
    {
        static void Main(string[] args)
        {
            string text;
            System.Console.WriteLine("Loading start...");
            using (var reader = new StreamReader(@"../../../output.txt"))
            {
                text = reader.ReadToEnd();
            }
            System.Console.WriteLine("Loading complete!");
            var list = text.Split("\n").ToList();
            int all = list.Count();
            int sum = 0;
            System.Console.WriteLine("The list complete. (" + all + " words)");
            File.WriteAllText(@"../../../freq.tsv", "");
            while (list.Count > 0)
            {
                var s = list[0];
                int cnt = list.Count(i => i == s);
                sum += cnt;
                System.Console.WriteLine(string.Format("{0}\t{1, 10}\t{2:0.000}%", s, cnt, ((double)sum / all * 100)));
                File.AppendAllText(@"../../../freq.tsv", s.Trim() + "\t" + cnt + "\n");
                list.RemoveAll(i => i == s);
            }
        }
    }
}
