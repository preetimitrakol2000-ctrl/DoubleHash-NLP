from tokenizer import extract_tokens
from intent_match import CommandIntentMatcher

if __name__ == "__main__":
    print("🧠 Initializing Localized DoubleHash-NLP Command Core...\n")

    security_profile = CommandIntentMatcher()
    security_profile.train_phrase(extract_tokens("activate enable system security lock vault arm surveillance"))

    user_voice_command = "please activate the surveillance system immediately!"
    parsed_input = extract_tokens(user_voice_command)

    matching_hits = security_profile.assess_score(parsed_input)

    print(f"📝 Raw Voice Transcribed Line: \"{user_voice_command}\"")
    print(f"🔮 Map Matching Intent Core Intersections: {matching_hits}")
    if matching_hits >= 2:
        print("💡 Action Verdict -> [EXECUTE DEVICE SYSTEM STATE TRANSITION LOOP]")
    else:
        print("❌ Action Verdict -> [DROPPING PATTERN UNRECOGNIZED ROUTE]")
