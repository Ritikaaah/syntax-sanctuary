import time
import sys

def slow_print(text):
    for char in text:
        print(char, end="", flush=True)
        time.sleep(0.02)
    print()

def init_state():
    return {
        "name": "Detective Aria Quinn",
        "clues": set(),
        "visited": set(),  
        "accused": None,
    }

def divider():
    print("\n" + "-" * 50 + "\n")

def arrival(path):
    divider()
    slow_print("You are Detective Aria Quinn, called to Blackwood Manor, where the wealthy industrialist Victor Blackwood was murdered at midnight during a thunderstorm\n. What will you do?")
    slow_print("1) Inspect the body")
    slow_print("2) Question the family and staff")
    slow_print("3) Search the crime scene room (study)")
    slow_print("4) Review collected clues")
    slow_print("5) Make an accusation (accuse a suspect)")
    slow_print("6) Quit the case")
    choice= input("Choose a number from 1-6: ")
    if choice=="1":
        inspect_body(path)
        return
    elif choice=="2":
        question_family(path)
        return
    elif choice== "3":
        search_study(path)
        return
    elif choice== "4":
        review_clues(path)
        return
    elif choice== "5":
        make_accusation(path)
        return
    elif choice== "6":
        slow_print("You close the file on Blackwood Manor. The mystery remains unsolved.")
        sys.exit()
    else:
        slow_print("Invalid choice. Try again.")
        arrival(path)

def inspect_body(path):
    divider()
    path["visited"].add("inspect_body")
    slow_print("You kneel beside Victor's still form on the study floor and observe:")
    slow_print("- Blunt force trauma to his head.")
    slow_print("- A faint smell of almond oil.")
    slow_print("- His missing pocket watch.")
    path["clues"].add("almond_oil")
    path["clues"].add("missing_pocket_watch")
    slow_print("1. Ask the doctor about the almond smell\n 2. Ask the butler about Victor’s pocket watch")
    choice= input("Choose a number from 1-2: ")
    if choice== "1":
        talk_to_helena(path)
        return
    elif choice== "2":
        ask_butler_for_watch(path)
        return
    else:
        inspect_body(path)

def talk_to_helena(path):
    divider()
    path["visited"].add("talk_to_helena")
    slow_print("You find Dr. Helena in the corridor, fidgeting.")
    slow_print("You mention the almond oil; she explains: 'Victor used almond-scented massage oil.'")
    slow_print("She seems nervous and avoids your gaze.")
    slow_print("You notice a missing medicine cabinet key in the doctor's belongings.")
    path["clues"].add("missing_cabinet_key")
    slow_print("\nChoices:")
    slow_print("1. Search the medical room\n 2. Accuse Dr. Helena directly")
    choice= input("Choose a number from 1-2: ")
    if choice== "1":
        medical_room(path)
        return
    elif choice== "2":
        accuse_helena(path)
        return
    else:
        talk_to_helena(path)

def accuse_helena(path):
    divider()
    slow_print("You accuse Dr. Helena abruptly. She panics and tries to run.")
    slow_print("In her bag you find sedatives. She claims she only kept them for Victor's insomnia.")
    path["clues"].add("sedatives_in_bag")
    slow_print("Outcome: Helena is detained temporarily but insists she didn't kill Victor—she only helped medicate him.")
    slow_print("This premature accusation may have cost you a better lead.")
    path["visited"].add("helena_detained")
    arrival(path)

def medical_room(path):
    divider()
    path["visited"].add("medical_room")
    slow_print("You search the locked medical room (you find a spare key). Inside you find:")
    slow_print("- A bottle of sedatives")
    slow_print("- Torn fabric matching a dress")
    slow_print("- An empty vial of almond-scented oil")
    path["clues"].add("sedatives_in_medical_room")
    path["clues"].add("torn_fabric")
    path["clues"].add("empty_vial_almond_oil")
    slow_print("This links Dr. Helena and Evelyn in some way.")
    slow_print("\nChoices:")
    slow_print("1. Confront Evelyn with the torn fabric\n 2. Confront Dr. Helena with the sedatives\n 3. Only observe them quietly")
    choice= input("Choose a number from 1-3: ")
    if choice== "1":
        confront_evelyn(path)
        return
    elif choice== "2":
        confront_helena_with_evidence(path)
        return
    elif choice== "3":
        slow_print("You decide to observe their behavior, hoping someone slips up.")
        path["visited"].add("observed_evelyn_helena")
        arrival(path)
    else:
        arrival(path)

def confront_evelyn(path):
    divider()
    path["visited"].add("confront_evelyn")
    slow_print("You bring Evelyn into the study and ask about the torn fabric and oil.")
    slow_print("She is cold but cracks when presented with the evidence; her dress is stained with almond oil.")
    path["clues"].add("dress_stain_almond")
    slow_print("Under pressure she admits Victor hinted at a divorce and had been distant.")
    slow_print("\nChoices:")
    slow_print("1. Press Evelyn for motive and timeline\n 2.Let Evelyn go and investigate elsewhere")
    choice = input("Choose a number from 1-2: ")
    if choice == "1":
        slow_print("Evelyn says she was in her room at midnight but admits she left the house earlier that night to walk the grounds; she returned and discovered Victor.")
        path["clues"].add("evelyn_alibi_weak")
    elif choice== "2":
        slow_print("You decide not to press Evelyn further for now.")
        arrival
    else:
        slow_print("Invalid choice.")
        confront_evelyn(path)

def confront_helena_with_evidence(path):
    divider()
    path["visited"].add("confront_helena_with_evidence")
    slow_print("You present the sedatives and torn fabric to Dr. Helena.")
    slow_print("She grows defensive but allows you to search her bag; the sedatives are in a prescribed vial (but not prescribed to Victor).")
    path["clues"].add("sedatives")
    slow_print("Helena says she gave Victor medication before bed; she denies involvement in foul play.")
    arrival(path)

def ask_butler_for_watch(path):
    divider()
    slow_print("You ask Marcus about the pocket watch.")
    slow_print("Marcus fidgets, admits Victor kept many items hidden; his hands show bruises.")
    path["clues"].add("bruised_hands")
    slow_print("\nChoices:")
    slow_print("1. Press Marcus harder\n 2. Search Marcus's room\n 3. Check CCTV")
    choice= input("Choose a number from 1-3: ")
    if choice== "1":
        press_butler(path)
        return
    elif choice== "2":
        search_butler_room(path)
        return
    elif choice== "3":
        check_CCTV(path)
        return
    else:
        slow_print("Invalid choice.")
        ask_butler_for_watch(path)

def press_butler(path):
    divider()
    slow_print("Under pressure Marcus admits he argued with Victor last week but swears he didn't kill him.")
    slow_print("He mentions a secret midnight meeting Victor had planned.")
    path["clues"].add("butler_knows_meeting")
    arrival(path)

def search_butler_room(path):
    divider()
    path["visited"].add("search_butler_room")
    slow_print("You search Marcus's room carefully.")
    slow_print("You find Victor's pocket watch hidden under a loose floorboard and a torn note reading 'Meet me at MIDNIGHT — I.M.'")
    path["clues"].add("pocket_watch_found_in_butler")
    path["clues"].add("torn_note_im")
    slow_print("This implicates Iris Monroe.")
    arrival(path)

def check_CCTV(path):
    divider()
    path["visited"].add("check_CCTV")
    slow_print("You attempt to check the CCTV footage. The system is disabled around midnight.")
    path["clues"].add("cctv_disabled")
    path["clues"].add("security_feed_erased")
    slow_print("Only someone with access to the system could erase footage. You recall Lucas handled systems sometimes.")
    arrival(path)

def question_family(path):
    divider()
    path["visited"].add("question_family")
    slow_print("You gather the residents in the drawing room: Evelyn (widow), Lucas (son), Iris (business partner), Marcus (butler), Dr. Helena.")
    slow_print("\nWho do you question first?")
    slow_print("1. Evelyn\n 2. Lucas\n 3. Iris\n 4. Marcus\n 5. Dr. Helena\n 6. Return to the main options")
    choice= input("Choose a number from 1-5: ")
    if choice== "1":
        question_evelyn(path)
        return
    elif choice== "2":
        question_Lucas(path)
        return
    elif choice== "3":
        question_iris(path)
        return
    elif choice== "4":
        ask_butler_for_watch(path)
        return
    elif choice== "5":
        talk_to_helena(path)
        return
    else:
        arrival(path)

def question_evelyn(path):
    divider()
    path["visited"].add("question_evelyn")
    slow_print("Evelyn meets your gaze with practiced calm.")
    slow_print("She says she and Victor had a strained relationship. She claims to have been asleep at midnight.")
    slow_print("You notice a small cut on her hand and the earlier torn fabric evidence could link her.")
    path["clues"].add("evelyns_cut_hand")
    slow_print("\nChoices:")
    slow_print("1. Check Evelyn's room\n 2. Observe Evelyn quietly\n 3. Ask Evelyn about divorce rumors")
    choice= input("Choose a number from 1-3: ")
    if choice== "1":
        evelyn_room(path)
        return
    elif choice== "2":
        slow_print("You watch Evelyn; she seems composed but distant.")
        path["visited"].add("observed_evelyn")
    elif choice== "3":
        slow_print("Evelyn reveals letters indicating Victor planned a divorce.")
        path["clues"].add("victor_planned_divorce")
    else:
        slow_print("Invalid choice.")
    arrival(path)

def evelyn_room(path):
    divider()
    path["visited"].add("evelyn_room")
    slow_print("In Evelyn's room you find a dress stained with almond oil and some hidden letters about the divorce.")
    path["clues"].add("dress_stain_almond")
    path["clues"].add("victor_planned_divorce")
    slow_print("She claimed to be asleep, but do these betray her?")
    arrival(path)

def question_Lucas(path):
    divider()
    path["visited"].add("question_Lucas")
    slow_print("Lucas is jittery. You learn of his large gambling debts and opportunity to access Victor's safe.")
    path["clues"].add("gambling_debts")
    path["clues"].add("safe_broken")
    slow_print("You notice Lucas has a small cut on his finger and you find tiny blood drops near the study floor.")
    path["clues"].add("blood_drops_Lucas")
    slow_print("\nChoices:")
    slow_print("1. Threaten to expose his debts\n 2. Tail Lucas secretly\n 3. Ask about CCTV access")
    choice= input("Choose a number from 1-3: ")
    if choice== "1":
        slow_print("Lucas gets defensive but reveals nothing more.")
        arrival(path)
    elif choice== "2":
        tail_Lucas(path)
        return
    elif choice== "3":
        slow_print("Lucas admits he knows the security system but denies tampering with it.")
        path["clues"].add("Lucas_knows_system")
        arrival(path)
    else:
        slow_print("Invalid choice. Try again.")
        arrival(path)

def tail_Lucas(path):
    divider()
    path["visited"].add("tail_Lucas")
    slow_print("You follow Lucas quietly and see him meet Iris in the gardens. They argue heatedly.")
    path["clues"].add("Lucas_meets_iris")
    arrival(path)

def question_iris(path):
    divider()
    path["visited"].add("question_iris")
    slow_print("Iris is sharp and defensive. She denies involvement in violence but admits business conflicts with Victor.")
    slow_print("You notice her heels have mud matching the garden, and there's a torn meeting note hinting at midnight.")
    path["clues"].add("iris_mud_heels")
    path["clues"].add("torn_note_im")
    slow_print("\nChoices:")
    slow_print("1. Visit Iris's office\n 2. Compare shoe prints")
    choice= input("Choose a number from 1-2: ")
    if choice== "1":
        iris_office(path)
        return
    elif choice== "2":
        slow_print("You compare shoe prints; they match prints leading out the study window to the garden.")
        path["clues"].add("shoeprints_garden")
        arrival(path)
    else:
        slow_print("Invalid choice.")
        arrival(path)

def iris_office(path):
    divider()
    path["visited"].add("iris_office")
    slow_print("In Iris's office you find a contract with her signature and notes suggesting a midnight meeting with Victor.")
    path["clues"].add("contract_iris")
    arrival(path)

def search_study(path):
    divider()
    path["visited"].add("search_study")
    slow_print("You examine the study thoroughly. Observations:")
    slow_print("- A window is half open; footprints lead outside to the garden.")
    slow_print("- A broken vase (blood on it) and blood drops that don't match the main wound.")
    slow_print("- A missing letter from Victor's desk.")
    path["clues"].add("window_open")
    path["clues"].add("broken_vase")
    path["clues"].add("missing_letter")
    slow_print("\nChoices:")
    slow_print("1. Follow the footprints to the garden shed\n 2. Reconstruct the scene for handedness clues\n 3. Analyze the blood drops with Lucas")
    choice= input("Choose a number from 1-3: ")
    if choice== "1":
        garden_shed(path)
        return
    elif choice== "2":
        reconstruct_scene(path)
        return
    elif choice== "3":
        analyze_blood(path)
        return
    else:
        slow_print("Invalid choice.")
        search_study(path)

def garden_shed(path):
    divider()
    path["visited"].add("garden_shed")
    slow_print("Following prints, you reach the garden shed. Inside you find rope, gloves, and a contract with Iris's signature.")
    path["clues"].add("rope_gloves_contract")
    slow_print("This points to Iris having some involvement or at least knowledge.")
    arrival(path)

def reconstruct_scene(path):
    divider()
    path["visited"].add("reconstruct_scene")
    slow_print("You carefully reconstruct the altercation. The wound angles, and the positioning suggest the attacker was left-handed.")
    path["clues"].add("left_handed_attack")
    slow_print("Only Evelyn and Iris are reported left-handed in the household records.")
    arrival(path)

def analyze_blood(path):
    divider()
    path["visited"].add("analyze_blood")
    slow_print("You analyze the small blood droplets and discover they match Lucas (a small cut on his finger).")
    path["clues"].add("blood_drops_Lucas")
    arrival(path)

def review_clues(path):
    divider()
    slow_print("You review the clues you've gathered so far:")
    if not path["clues"]:
        slow_print("No clues collected yet.")
    else:
        for c in path["clues"]:
            slow_print(f"- {c}")
    slow_print(f"\nTotal clues collected: {len(path['clues'])}")
    arrival(path)

def make_accusation(path):
    divider()
    slow_print("Who would you like to accuse?")
    slow_print("1) Evelyn")
    slow_print("2) Lucas")
    slow_print("3) Dr. Helena")
    slow_print("4) Marcus (butler)")
    slow_print("5) Iris")
    slow_print("6) Return to main options")
    choice= input("(1,2,3,4,5,6): ")
    accused= None
    if choice== "1":
        accused= "Evelyn"
    elif choice== "2":
        accused= "Lucas"
    elif choice== "3":
        accused= "Helena"
    elif choice== "4":
        accused= "Marcus"
    elif choice== "5":
        accused= "Iris"
    else:
        arrival(path)
        return
    path["accused"] = accused
    resolve_accusation(path)

def resolve_accusation(path):
    divider()
    accused = path["accused"]
    slow_print(f"You formally accuse {accused.title()} of murdering Victor Blackwood.")

    c = path["clues"]
    has = lambda key: key in c
    has_sedatives = (
        has("sedatives") or
        has("sedatives_in_medical_room") or
        has("sedatives_in_bag")
    )

    joint_conspiracy = (
        has_sedatives and
        (has("torn_fabric") or has("dress_stain_almond")) and
        has("empty_vial_almond_oil") and
        has("missing_cabinet_key") and
        (has("observed_evelyn_helena") or has("pocket_watch_found_in_butler") or has("butler_knows_meeting"))
    )

    helena_case = has("sedatives_in_bag") and has("missing_cabinet_key")

    evelyn_case = (has("dress_stain_almond") or has("torn_fabric")) and has("victor_planned_divorce") and (has("left_handed_attack") or has("evelyns_cut_hand"))

    iris_case = has("rope_gloves_contract") and has("torn_note_im")

    Lucas_case = has("blood_drops_Lucas") and has("safe_broken") and has("gambling_debts") and has("cctv_disabled")

    marcus_case = has("pocket_watch_found_in_butler") and has("bruised_hands") and not (iris_case or evelyn_case or helena_case or Lucas_case)

    perfect_detective = (
        has_sedatives and
        has("torn_fabric") and
        has("empty_vial_almond_oil") and
        has("pocket_watch_found_in_butler") and
        has("torn_note_im") and
        has("left_handed_attack")
    )

    if joint_conspiracy and (accused == "Evelyn" or accused == "Helena"):
        slow_print("As you lay out the evidence — sedatives, the almond oil traces, the torn fabric and the missing medicine key — the room goes silent.")
        slow_print("Evelyn breaks down and confesses: she drugged Victor; Dr. Helena helped medicate and covered tracks. They planned to make his death look like an accident and flee with insurance.")
        slow_print("Outcome: You solved the case — THE TRUE JOINT CONSPIRACY ENDING.")
        end_game_success(path, perfect=True)
        return

    if accused == "Evelyn" and evelyn_case and not iris_case:
        slow_print("You confront Evelyn with dress stains, torn fabric, and letters about the divorce.")
        slow_print("Under interrogation she confesses to drugging Victor and staging scenes to mislead.")
        slow_print("Outcome: Evelyn arrested. (Evelyn Ending).")
        end_game_success(path)
        return

    if accused == "Helena" and helena_case:
        slow_print("You present the missing medicine key and sedatives found in Dr. Helena's bag.")
        slow_print("Helena confesses she provided medication and later helped hide Victor's body, but says she did not strike the fatal blow.")
        slow_print("Outcome: Helena detained and charged for accessory to murder. (Helena Ending).")
        end_game_success(path)
        return

    if accused == "Iris" and iris_case:
        slow_print("The rope, gloves, and the contract with Iris's signature are compelling.")
        slow_print("She admits to meeting Victor but insists it was about the contract. However, evidence places her at the shed where incriminating items were found.")
        slow_print("Outcome: Iris arrested for complicity. (Iris Ending).")
        end_game_success(path)
        return

    if accused == "Lucas" and Lucas_case:
        slow_print("Lucas's debts, the broken safe, the blood traces, and CCTV tampering make a convincing case.")
        slow_print("He confesses partially — that he intended to confront Victor about money but denies murder. However, the evidence lands him as the prime suspect.")
        slow_print("Outcome: Lucas arrested, but doubts remain. (Lucas Ending).")
        end_game_partial(path)
        return

    if accused == "Marcus" and marcus_case:
        slow_print("Marcus had Victor's pocket watch and bruises — suspicious. He admits to hiding the watch to protect Lucas.")
        slow_print("Outcome: Marcus cleared of murder but reprimanded. (Marcus Ending - innocence).")
        end_game_partial(path)
        return

    if perfect_detective and accused in ("Evelyn", "Helena"):
        slow_print("Your careful collection of evidence shows a complete thread: the sedatives, the torn fabric, the pocket watch, the midnight note, and the handedness match.")
        slow_print("You accuse them both and they are brought to justice together. PERFECT DETECTIVE ENDING.")
        end_game_success(path, perfect=True)
        return

    slow_print("You present your accusation, but the evidence is thin or contradictory.")
    slow_print("The accused denies involvement. Subsequent investigation shows your accusation was premature or mistaken.")
    slow_print("Outcome: Wrong Accusation. The true killer remains free... for now.")
    end_game_failure(path)

def end_game_success(path, perfect=False):
    divider()
    if perfect:
        slow_print("YOU WIN — Perfect closure. The duo is convicted and the truth comes out.")
    else:
        slow_print("CASE CLOSED: Good detective work. The accused is arrested and the immediate threat is neutralized.")
    slow_print("\nFinal summary of collected clues:")
    for c in sorted(path["clues"]):
        slow_print(f"- {c}")
    play_again_prompt()

def end_game_partial(path):
    divider()
    slow_print("The case is partly solved; arrests were made but certain inconsistencies remain in the evidence.")
    slow_print("Summary of collected clues:")
    for c in sorted(path["clues"]):
        slow_print(f"- {c}")
    play_again_prompt()

def end_game_failure(path):
    divider()
    slow_print("You failed to pin the killer. The real culprits slip away amid the confusion.")
    slow_print("Summary of collected clues (what you did find):")
    for c in sorted(path["clues"]):
        slow_print(f"- {c}")
    play_again_prompt()

def play_again_prompt():
    slow_print("\nWould you like to play again? (y/n)")
    ans = input("> ").strip().lower()
    if ans.startswith("y"):
        main()
    else:
        slow_print("Thank you for playing Blackwood Manor. Goodbye.")
        sys.exit()

def main():
    path = init_state()
    slow_print("\n=== THE MIDNIGHT MURDER AT BLACKWOOD MANOR ===")
    slow_print("You are Detective Aria Quinn. Solve the murder before daylight.")
    slow_print("\nResidents present: Evelyn (widow), Lucas (son), Dr. Helena (physician), Marcus (butler), Iris (business partner).")
    slow_print("Tip: Inspect, question, and gather multiple clues before making an accusation.")
    arrival(path)

if __name__ == "__main__":
    main()