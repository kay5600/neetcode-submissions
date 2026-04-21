public class Solution {
    public bool IsAnagram(string s, string t) {

        if(s.Length != t.Length)
        {
            return false;
        }
        Dictionary<char, int> dict1 = new Dictionary<char, int>();
        Dictionary<char, int> dict2 = new Dictionary<char, int>();
        foreach(char i in s)
        {
            if(!dict1.ContainsKey(i))
            {
                dict1.Add(i,1);
            }
            else
            {
                dict1[i]++;
            }
        }
        foreach(char i in t)
        {
            if(!dict2.ContainsKey(i))
            {
                dict2.Add(i,1);
            }
            else
            {
                dict2[i]++;
            }
        }

        return dict1.Count == dict2.Count && !dict1.Except(dict2).Any();

    }
}