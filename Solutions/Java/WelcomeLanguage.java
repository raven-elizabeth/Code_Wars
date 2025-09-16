package Solutions.Java;

// Your start-up's BA has told marketing that your website has a large audience in Scandinavia and surrounding countries. 
// Marketing thinks it would be great to welcome visitors to the site in their own language. 
// Luckily you already use an API that detects the user's location, so this is an easy win.
// The Task: Think of a way to store the languages as a database. The languages are listed below so you can copy and paste!

// Write a 'welcome' function that takes a parameter 'language', with a type String, and returns a greeting - if you have it in your database. 
// It should default to English if the language is not in the database, or in the event of an invalid input.
// The Database:
// [ ("english", "Welcome"), ("czech", "Vitejte"), ("danish", "Velkomst"), ("dutch", "Welkom"), ("estonian", "Tere tulemast"), ("finnish", "Tervetuloa")
// , ("flemish", "Welgekomen"), ("french", "Bienvenue"), ("german", "Willkommen"), ("irish", "Failte"), ("italian", "Benvenuto"), ("latvian", "Gaidits")
// , ("lithuanian", "Laukiamas"), ("polish", "Witamy"), ("spanish", "Bienvenido"), ("swedish", "Valkommen"), ("welsh", "Croeso")]

// Possible invalid inputs include:
// IP_ADDRESS_INVALID - not a valid ipv4 or ipv6 ip address
// IP_ADDRESS_NOT_FOUND - ip address not in the database
// IP_ADDRESS_REQUIRED - no ip address was supplied


// My solution:
import java.util.HashMap;
public class WelcomeLanguage {
    public static String greet(String language){
        HashMap<String, String> languageDB = new HashMap<String, String>();
        languageDB.put("english", "Welcome");
        languageDB.put("czech", "Vitejte");
        languageDB.put("danish", "Velkomst");
        languageDB.put("dutch", "Welkom");
        languageDB.put("estonian", "Tere tulemast");
        languageDB.put("finnish", "Tervetuloa");
        languageDB.put("flemish", "Welgekomen");
        languageDB.put("french", "Bienvenue");
        languageDB.put("german", "Willkommen");
        languageDB.put("irish", "Failte");
        languageDB.put("italian", "Benvenuto");
        languageDB.put("latvian", "Gaidits");
        languageDB.put("lithuanian", "Laukiamas");
        languageDB.put("polish", "Witamy");
        languageDB.put("spanish", "Bienvenido");
        languageDB.put("swedish", "Valkommen");
        languageDB.put("welsh", "Croeso");
        
        
        language = language.toLowerCase();
        
        return (languageDB.containsKey(language)) ? languageDB.get(language) : languageDB.get("english");
    }
}

// Alternative:
// return languageDB.getOrDefault(language, map.get("english"));
