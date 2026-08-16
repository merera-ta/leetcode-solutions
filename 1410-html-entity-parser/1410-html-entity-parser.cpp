#include <string>
#include <unordered_map>
using namespace std;

class Solution {
public:
    string entityParser(string text) {
        unordered_map<string, string> entities = {
            {"&quot;", "\""},
            {"&apos;", "'"},
            {"&amp;", "&"},
            {"&gt;", ">"},
            {"&lt;", "<"},
            {"&frasl;", "/"}
        };

        string result;
        result.reserve(text.size());

        for (size_t i = 0; i < text.size();) {
            if (text[i] == '&') {
                size_t end = text.find(';', i);

                if (end != string::npos) {
                    string entity = text.substr(i, end - i + 1);

                    auto it = entities.find(entity);

                    if (it != entities.end()) {
                        result += it->second;
                        i = end + 1;
                        continue;
                    }
                }
            }

            result += text[i];
            i++;
        }

        return result;
    }
};