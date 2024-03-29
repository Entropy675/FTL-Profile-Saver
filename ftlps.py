#!/usr/bin/env python

import os
import subprocess
import argparse

from datetime import datetime

# Config:
savesPath = 'saves\\'
aeSave = "ae_prof.sav";
contSave = "continue.sav";

def copyAndRename(src, dest, newName):
    try:
        # Combine the destination directory and the new name to get the full path
        newPath = os.path.join(dest, newName)

        # Copy the file to the new path
        with open(src, 'rb') as sourceFile, open(newPath, 'wb') as destinationFile:
            destinationFile.write(sourceFile.read())

    except FileNotFoundError:
        print("Source file not found.")
    except PermissionError:
        print("Permission error. Make sure you have the required permissions.")
    except Exception as e:
        print(f"An error occurred: {e}")

def drawNebula():
    print("\n                             This is the nebula profile saver for Faster Than Light.");
    nebulaPic = '''
^><>>>>>><<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>><>))))<<<<<<<<<>>>>> 
[(><<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>><>><>>>>>>>>>>>>>><>))<)<<<<<<<<<>><>><>>>>><>>>>>><<< 
[[][(<>>>>>>>>>>>>>>^>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>><<><<)<<<<<<<<>]#{#[[>>>>>>>>>>>>>><< 
(([}}]([)>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>^>>>>>>>>>>>>>>>>>>><)<<<)<<<<<<<<>>>>>>){#%#{}<>>>>>>>>>>><< 
(}}][#[{[<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>><<))))<)<<<<<<<>>>>>>>>>}[}{(>>>><>>>>><<<< 
]][]{#{##>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>><))<<))<)<<<>>>>>>>>>>>}{){{{>>>>>>>>>>>>> 
([[[}#{{<^^>^^#}{())>>>>^^>>>>><<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>)))))))><))<<<<<<>>>>^^^>>)<[(^^^>>>>>>>>>>><< 
[}}}}}}{(>>>^){}#%{]{{()>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>))))))<<<<)<><<<<<<>>({][{(##)^>^>>>><>>>}#{{%# 
([[[([]]^>>>>>><}](<^>^^^^>>>>>^^>>>^>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>)<))<<>>>>>>>>>>>>>>>[})>>>{}}[^^>>>>><<}([###]{ 
<(]]]]][[][(>>>>%<#{)[[^^^>^(]]}}[(}]{{(^>>>>>>>^>>>>>>>>>>>>>>>>>>>><<<<<>>>>>>>>>>>>>>>))>>^{<}#[>>>>>>>>>>){[####[} 
)(((]((]]([}]]]<]}]{])()(](][{##{}}}]{}}]>>>>>>>>>^^>>>>>>>>>>>>>>>>><<<<<<>>^^[[]}}(<#>>^>^>>>>^}[)^{<>>>>>^>>{##[{## 
)]((]}]}][[]][()(#)}(](]<][{{}}#%%{{[%%[><>>>>>>>>>>><<<<))<<<>>>>><<<<>>>>>>{[#}>}<#<#[#<>^^>}}}}>>><([]>^>}#}{[}{[}] 
][]][{}}}{{[]([%}@}}{#((}[}{#{{}[}}[}{{[#}%%[^>>>>>>>>>))))))))<><>>>>>^>>>>^>[{[()^}]]^>)}[<#]>>(>>^^([[]>]#{#{#{}[}[ 
)]][[[[{[{][[[]]}%})#[)%]#}{}([](]###%%#{[]#%{[>>>>^^>>><))<)<[<()))>>>^>>>>>))(#<^}(><<[]}<}{{>>}^>^^^^}^)>{#{{[{}([} 
]}[}]{[}}}}[]()[%]}]([(}]({}[}[(}][][@}}]}}{{}>>>>>>>^>>><>><<)))>)^>>>>>>>^>{]<^^>])>^^>[^^^^((>}^>^>^>(}}({}}{}}}]() 
[}{#{##{{]])}#}%{%#}[[(]]{}[}[[}#}{[%{{^[)]}[})>>><<<<<>>>><<<)<)](<>>>>>>>)(>>^>>>>^>^^^]>[{[##}{{{}[^(}[{}#####[]((( 
{#}())[}[{#]}]%(#{])((][((#{([(}[}##%%]}#>^><><>><<<>>>><><)<<)))((>^>><<<>><>^^><>>>^>}}{%%@#{%%}@%%}##%#{}##{{}}(])) 
(](])]]((()(]]#))({)(}][}}][]<){#}}{([{}{>>>>>^>>>))]><>><<<<<<))()))>>))<<>)<^^>>>>({%%@%@%%%{%#%{{%#]##{]}}}[[}]}])) 
)((][](]])((({((()({%[}#{[]]({{%###{}}#%#{((>>>>>><](()<><<<<<<(((>>><<<)><<<<><>><>^(]%#%{}%%%%%%%%%%#%##}[[](])()))< 
#%#}}]][)([][})(}#{{{{{}}{#}#%%@@##}{[}%}{###^^><>)))<<<<<<)<^<))<<>^>))<>)))>>>>><>>^[#%%{%@%#{}}{######{[[][(()<<<<< 
%%#{)(][([]}}[]]#%{%%%%{[}{[%#%%@##%%}{##]}{#>>><<)()]()))<)>>>(()>^^<>))<><<<)<><()>##{%{#@%{}][[]]]](}#%%}}]}[))<)<> 
(}}([}[}}]}}#])(]{#%%@#%}]]]]##%%%@##[}#(]}{{>><<<)(([]](((()><(<)<^^><%(>)<{%%{#%%%%#}})]#%@#[[][(}]]](###{{{#}](]<)) 
]([{##[[#{[]#{}((({%@{{}{{[}}}()%@%%][))*]]}{)<)>><]()<))((<>><<<)<<^^%@@%@^@@@@@@@%{[]]}#]{%%{[([{{[]][{{((]}[}{}]]]( 
})(}###%%####[])({#@%##%%%%{[[)<@%#}%>^>^>>>><<>()>(>^[]]]](}[>^^^^^*)%@@@]>[@@@@@@%}{%##%{%#}((]](]](]]])](((][]]]][( 
{]((#{{@#%[#%%%}%@%%%{{{[]}%%%}<%]}#{}#}><<<<))()))][>>)})]([)>()^({##{{#}{[%@@%{{@%}]}}}##@%}}[[][]][}]]]]]](]]](](]( 
[#%%#%%%#}%[[}#{{%%@%#}{{{{{#{{(%}}%)}[[>)^^)(<)])[(}[)>>[{)}]>^^^{[]@#{{{%%[{%{}#@(}}[}}{{#@%%{]}(}]}[[[[(]]())<<)))< 
[(]]%%%%%%{}[{}{{#{{%%%%{}{[[(}(}{{@{#}^><<<>>({{(}]{]^<>>)><>^>)>>[{}#%}}{%}[[[[%@@%#%{}[{#%{}}[[#(]}}}[[][()))<<>>>> 
[[]]({%%#%%}}(<[#%#{%}@#{#{]}{}]}@{@@<^^^>>>>>>({^*]){{{}[}>>[>())^^<@@{{}[}#%{#}%@@@%}}}}{{[][(([}[][[]](])<)>>>>>>>> 
]((}[()#%#}{(]]#%%#{}#{@%@##}#]}}%{%@})<>()^>]>]})]{[>^^^^>^^<<^>>][[@@%%#{}}%{[[@@@@%@%%%@@(]{)[}[[}}{}[(]])<>>>>>>>^ 
(}#}))()##[{{)(]#{#{[](]][[}[[]][%%%@{]>>}]<^^(}})^*^*^>{####^>>]]{{)@%%#%#@{@]}##%@@%])[[{#%{[[]{}[}[}[[]]])))<>>>>>> 
%%%%%#{###{[]([<[#@}%[]{[(}[{[{}[%#%@}#<<}})(](>^^^^#]#][><<]([^[{]<(@%###@@@[](}[{%]([{#%@%###{{#%}{[[}]]]]]][]]()<)< 
#@@@%###{}{#{[<][{{%[[{])>#}{}][[#{#@@%((}}<>^^^)##%}{}}%}}<}{}^^>}%@%#{}%@@@#{{}{[{]{]%%##[#}#@@@@@@@}{[]]}]}]{{[]))( 
@#%@#@@%}}{{}(<<(##@%#}]<>#}[[[}[}##@@@%]<^^^^%#%{###{#{{]%{#]^>^^@@@}{#%%@@@)]([{{[{]#@@%[[}{@@@#@@{{##[{][[[}({[[{[{ 
#[}%%%@#@@#%{(]]}#%#{{%(>>##][[[[###@@@@@%%^^^@@@@@{%{@{%%@@@@>>>>@@@}###%@@@([{{{[]]{#@@[](%@@@@@@@#][}][}{%}#][]}[]] 
}[}{{}#@#@#%[[](}}@{{@([<(([[(}{####@@@@@@@+==~^^@@@@@@@@@@@@#+-=)@%@%%{%@@@@(][}}%{{%%%#@%@@@@@}{#[#{%%{#%@%%%%#}#[}{ 
{{}}{}}%#%##[[}[(([#%[}#]<{%{{)]}#{{{@@{{@@@^>>>==(@@@@@@@@]=^~=@@@%@@%%@@@@@{[]([]{{]%%%#@%@@%@{}[[}}%%%%%%%}%}}}(][} 
}]{{[%@%##%#}%{[(}{}}{{][<[(#}{[{###{{@@%@@@@(+^+=++@@@@@@+^<+<=@@@@@@{%@@@%@{{]]}[<({(%#%@@@%]](}[#%@%@@{%@@@[[[{[#[[ 
[]}{{@@%#%{##{(}}%{]{[#}{{}[<%%##%%%{#@@@@@@@{]*+++=<#@@%~=^*>((@@@@@@@#@@@@[{({}}})((#{%%%@@}%[{[}#@@@@%]{[%{{]#}}[(% 
}{[##%##@}}%}#[{})#@[}[%{[)}()]@%{%%#{}@@%@@@@@*++*~^)}({^<[)@{[@@@@@@}%@%#@%@][({>)()[}%{[@@@@@@@%@@}[}#[})([[[[)][[[ 
{{}#}{[%{}#{}%%{()#{{%{{}}([][)%@%##{#{@@@@@@@%:+~+**+++++^(]%]%@@@@@@#@%{%%#%(}]})(({[}#{#@%{]<[)]##{{{%}](}]](](](() 
#{}}[#]}#%{[]##{[(>[{{}{}#]]{[(@@@%##%%@@@%@@@@<=~~~:~-~=+-~-~*@@@@@@@@%%#%%{@(]]}<)]([[###@@}###%[#@#%##}]]](][}[]]]( 
]}]##%%#[%%{}{{[#]]^#@(]}[)]{<}#@@@#%%%@@@@@@@@]^>=*==~~*++****#@@@@@@@@%%@%#@}][{<<()){#}##%@[{##@@##}{%#]}]{)[)][[]( 
()%@@#%%{[@%}[#}#}](>%%#[[(({}](}@@%%%#@@@@@@@@@*+++=++-+~~+=>^{@@%@@@@@%%%@@@@#[}(<]({@@@@@@@@%}%%%{{#@#[]}}[]([[}[[{ 
)%@%%%#((>%}}#(#%}}[>#][}}}[[}%]{@@@@%%@@@@@@@@@)+=***+**~*>>>)@@@@@@@@@@@@@@@@%}#[)[]#{}#{}@@%##][[}#@@@@{%}]{{{{#}[# 
(%%%%[}])]##%#]]##[([<[]}#%}[{@]}@@@@%%%@@@@@@@@[[<=**~^+*==*>[@@@@@@@@@@@%@@%]}[{%@#[)(]]#{@{%%%([))}@%%%%#%%%}{}}][[ 
)%@@@{%{(>[%@@{[]@{][)%@[}#}[]%#}]@@@@%%@@@@@@@@(}(=++<*^><^<[{@@@@@%@%@@@@@%}#}[[@%])(]{{%%{##]#%]}{)}(%}%{%%}][##}]} 
<#%%%{[>{(]>%%#}]%](}})@({}[]]%{%}@@@@%%@@@@@@@{>(<>+++++++=>)]%@@@@@@@%%{%%%@%[%{%^])><[#%]({>()%%%%*[#{[}%[}]#}{#{(% 
(@@}#[[){})[%{[}}%{<{[[@%%]#{}%{}{@@@@@%@@@@@@@%([]^*+=~~=^*^<(@@@@@{@@@#{##%%%@@@@%<]>]}%[([%%(](}}%[{}{{}}%{%%#%#}%% 
#%{}{{])<{)(%#{[%%{<#}%@##[}%{#[{@@@@@@@@@@@@@@[())^>*>+^^**+*>@@@@@%%@%@%@%%@@@@@@@{([>({[]%[#(](}#>[{%%#@{#@%##%%@{% 
}@%%{%{]<{(^@%#%%%%(#][@##{##}%{#@@@@@@@@@%@@@@[>)^*+=~^**^*>){@@@@@%@@@@%@@@@%#%}#%})]>(#<]#%}{%][#>#{@@%@@%%%%@@@@@@ 
*{#%%%{]}%}@}#@@{{%]%[{#%%%%###@@@@@@@@@@@@@@@@](<+=^^=*+=*=+(*(@@@@@@@@@@@@@@%##%%%})(<]#{^{{][%{[{[][#<>#%#%{{#@@@@@ 
^}<<}%%{}%%{{%{}#}###@{[#[[{%#%@@@@@@@@@@@@@@@]><](*>>~+*=*=+(]{@@@@@%@@@@@@@%{#%%@%()}>)]#%{}#{#]({#@@[<))%@%{}({@@@@ 
]{()]%##}%#}}}%<)(<<{@]]}))<(#{{%@@@@@#((%@@@%[)>>><>>+>>^<<]><[])@@@@@@@@@{{%%%@@@@)){)}}[%]>}#)][]}@%>}}{%@{#%}{@@@% 
%{()<##{[##}#%@[()}(<]}][[[[[[)}{{###%)^><^===<<<^*+<+>^<<>(]%{[#{(@@@@@@{}#%#%@@@@@)]{<(]({#%@<]}#)<{%<(<{%@%)[{#{{@@ 
#[)<(%%#](}#>>%##(]<)({()]>#[]#}[{#@@{{##<+^***++=-+~+*))=>=<>]])>@%@@@{#%#%@@@@@#[(]}{<]{[}][%<(#%<])#(}<}%#%<[<(}#@@ 
]()<]%{(][([}]][[[())]}[<}){{[#}[%#@@{{#@@@]>^^*~*^^^^+*++*^>+*<]{([#@{%%%@@@@@%%[[{#%%)([}][%#>[}#)([%[])#%%#{[<[{%@{ 
)<[<>#}{#{([}]]]}](](]]]<](}{{[][}@{#{@}#@@@%+~=--~~^>^^^^<>>+<[])%@@@@@@@@@@@#%(%%[{#@(](})[{%]<]%#>%{)([%}%##<<[#@%@ 
((])<{%}{[[##}{#{[[((]]]<{[}{{[(%}{}%]@#@@@%@@*+==+=+~===++=*<)+=<@@@}@@(@@@@{[{[[[}}#@(([][[]{##]%@%%#)(}%%}{%#%[{@@@ 
)<]<>)]{]}]%%}{#[[([[}[))}{}][[(]@[[}{%#}@@@@@{]^*+++~+=+=+=+~*][[@@@}@@)@@@@}}}}}[}}%%#[]>[[{[##)}<#>{)([#%(<%%#{%#%@ 
[]()<[}%####%#}}]]([[[)]([}}[}}[{%#}{@@@@@@@@@]%>^++*><*^^+=~*^>*}@@@#@@#@@@{##[}{{{%#%#)(][}[%%%]%){<))([{})>]#%]#%@@ 
[]))<){#{{##%%[%]()([])<)}{}[[{[#}@{#@%}@@@@@@@%>}[*=+*^~==~=~~+=+@@@{@@%@@%%%%{{{{{%{{@][])}##}(}#<{>])[}{[)[{@@@@#[} 
[())<]%@{{[#%#[#][)([])<){{[][}[}##%@@%@@@@@@@@]%{()<<>+++=++~~+>>%@@>@}@@@###@{{{#{@}#{#()[[##[([#{{<(({%#<){{#%@@@#] 
#]]()<#})#%%#%##]})())<<(#{}](#{{%%@@@@@@@@@@@@@{^}{>>^>*+++=~==**^<##@{@@@@@@@%{{}{%{@%%}<{}%%)](#%})(}#{)()[%#@@@@[{ 
@#](<>#][#@@%%%%[[)())<<<}}[][#}]#%@#%%@@@@@@%%{}})[)])++=~**=--=++{%^#{@@@@@@@#%{{@{%@%@@)%#@#<<)%@#]((#{](]]{{@{]}[} 
%{}(<<#<[{(#@@%#[})))(<<]{}{}[{}{{#@@#@@@@@@@@@@]<#}+<)>^+*^^*=+~^)((]@{[@@@@@@@%@@@{#@@@@]%##%%)#([@](]}]]([[#{{%@%({ 
{##((<}#<))%@%[{]{(())<(>%{#}}{]%##@@%@@@@@@@@@@[(^^*^>)^+++*^>^**^^[[@<>@@@@@@@[]%{@@@@@]{{%%#%]%]{%%]}{([](]{%{#{%@@ 
@#]([)<>>)(###[{}[(](<))<%%#{{%}%{{%%@@@@@@@@@@{%}(^^^>++>>**^<^+^=<}@@#@{@{#{@}%]%#@@}<][{#{%{#@@)}#@#]}[{((])%{#}[@# 
@##}{))>]>]##{}#[]]](<)]])%#{%%]%{%@@@@@@@@@@@{}{[(]<())<)><^<^+^*^<*={@@@@%}{#{#%%}[((([}[#{#%%%@[#%%)([}{})}(}%##}@# 
{{}{{])>)>)]%#{#[[[[](]([[##%@%#{@@@@@@@%@@@%^-~-~*+--+~==++=~>)]^[[{%@@@@#%}%[{#(]}}((})[][}{{#@@>]%@#<]{{#][)[{#{[## 
]][{[<<>(<(>[#%%}][[]]]]][%#{@%@@@@@@@@@@@[+-^)=++^*^=+*=~*<)]{%}+@@@@@%@%{#[{}#@<){([[})(]}}#%%#)<[%%%#(#%#][(]%%#%[@ 
#]))[(>([()<%%%@[[}}[[](]{@@@%%%%@@@@@@@@%<**++*^=~++++^>][]@%^#@@@@@@@%{#%#]##%%<<()[[[)([#{@@@#)[<#%%%#[##][(]@#}({% 
{)()()>[]](]}@@@}[{}{[]{#%@@@@%%@@@@@@@@@{)=*==+>>+=^*=^]]#@@@}#@@@@@@@#@@}][#{##<(]][[{([{##%{#<()<#%{[#(#%]}[]@#)]]} 
[([)<)<([#[[({@@{][}{[(%#@@@@@@@@@@@@@@@@#[]~~+=+^>^^)})]@@@@(@@@@@@@%%@@%{{}{{[#(]{{{}%[}{{%%#})(()#%{]%@%]][[]%{{}{} 
}))<<(<({[}}{)@@{{}[{[%@@%@@@@@@@@@@@@@<=*)<<*~=+)*^)<>{%{@@}@@@@@@@#@{@}[{[{}}]}]({#%#%}}{%@%%{)[]({%[}#%%%[[]{%#%%{% 
[]}%>()[#{}]}}@@@#{##%@%@@@@@@@@@@@@@@%*<^<)=*^><><^^^}(#@@%{#*@@@@@@@[[}#{)#}#}}{{]##%#}}{%%%%{)([[{#]}#)[#%{]#%#[#%} 
{(@@{<[{[[{]}{@%%}%#%@%#@@@@@@@@@@@@@@*=*^^+~*-**+>+<)])[@@)[@%@@@#%@{[{}{#(#%#(}%##%%@%[}{%%%%[)]]}{#)[#<){{(]#{{[{[%
}%%)))]}#[#]{#{@@%@@@%@@@@@@@@@@@@@@@@)~=*~*^~+*++)][{<{@{{%@@@@@@@@#{}{{{{[[#})]%%@@@@%}{{%%#>((([{{#(({<[#(]]}##[}#%
@@@#<]][{(#[{@#@@@@@@@@@@@@@@@@@@@@@@@%}]>)>*>>))<<()[@]]@@@(@@#@@@@@@%{#{#[[@@%[{@@@([%{##%@<})(]]{{{(<[#[{)(}{@@@%]%
@@}<}[([{]%##@%@@@@@@@@@@@@@@@@@@@@%%})*+^>+**^<(]]]]+)[#@@@@[@]@@@@@@##[#@@[@%%@@%@@([}]{%%#<((]](}{#])({#[(]([#[{%#%
@@{[}]<[[[%#{@@@@@@@@@@@@@@@{*+>=[*+=>=^<><^>=-~+~^>}#)@@@@##@@}@@@{[{#{[%@%}@@@@@%%##{{[[}#{><({][[{#{))}##)))###]##%
                                                                                                                   - S'''
    print(nebulaPic)
    print("\n")
    
def help(args):
    
    if(ensureSavesFolderExists()):
        drawNebula();
    # Instructions for different commands go here
    
    runname = os.path.basename(__file__).split(".")[0];
    
    commandList = [
    f"""
{runname} help:
    Displays nebula ascii and this manual.
    """,
    f"""
{runname} save [name]:
    Saves the current progress to the name specified. 
    """,
    f"""
{runname} load [name]:
    Loads the save with given name, if it doesn't exist
    it lists the ones that do (same as list) and does
    nothing else.
    """,
    f"""
{runname} list:
    Lists the saves locally stored in specified folder.
    """,
    f"""
{runname} run:
    Runs the game.
    """
    ]
    
    for command in commandList:
        print(command)
    return 0;
    
def ensureSavesFolderExists():
    # Check if the folder exists
    if not os.path.exists(savesPath):
        try:
            # Create the folder if it doesn't exist
            os.makedirs(savesPath)
            print(f"Folder '{savesPath}' created.")
            return True
        except OSError as e:
            print(f"Error creating folder '{savesPath}': {e}")
    return False

def save(args):
    if(ensureSavesFolderExists()):
        drawNebula();
    savefileAe_prof = args.name + "." + aeSave
    savefileContinue = args.name + "." + contSave
    
    print(f"Saving to file: {savesPath}{savefileAe_prof}")
    copyAndRename(aeSave, savesPath, savefileAe_prof);
    
    print(f"Saving to file: {savesPath}{savefileContinue}")
    copyAndRename(contSave, savesPath, savefileContinue);
    return;
    
def load(args):
    print(f"Loading from save: {args.name}")   
    
    savefileBackupAe_prof = "BACK." + aeSave
    savefileBackupContinue = "BACK." + contSave
    
    if(not (os.path.exists(f"{savesPath}{args.name}.{aeSave}") and os.path.exists(f"{savesPath}{args.name}.{contSave}"))):
        print("The name you chose was not found.")
        list("");
        return;
    
    print(f"Saving backup file: {savesPath}{savefileBackupAe_prof}")
    copyAndRename(aeSave, savesPath, savefileBackupAe_prof);
    os.remove(aeSave);
    copyAndRename(f"{savesPath}{args.name}.{aeSave}", "", aeSave);
    
    
    print(f"Saving backup file: {savesPath}{savefileBackupContinue}")
    copyAndRename("continue.sav", savesPath, savefileBackupContinue);
    os.remove("continue.sav");
    copyAndRename(f"{savesPath}{args.name}.{contSave}", "", contSave);
    
    return;
    
def list(args):

    saveNames = {}
    outputlist = {}
    try:
        files = os.listdir(savesPath)
        saveNames = {save: os.path.isfile(os.path.join(savesPath, save)) for save in files}
        
        if saveNames:
            prevName = "";
            for save in saveNames:
                if(prevName == save.split(".")[0]):
                    outputlist[save.split(".")[0]] = datetime.fromtimestamp(os.path.getmtime(savesPath + save));
                prevName = save.split(".")[0];
    except FileNotFoundError:
        print(f"Folder not found: {folder_path}")
        return None

    if outputlist:
        print("List of saves:")
        for name in outputlist.keys():
            print(f"  {name.ljust(25)} |\t (Last Modified: {outputlist[name]})");
    else:
        print("No saves currently stored.")
    
    return;

def run(args):
    subprocess.run(["start", "cmd", "/c", f"start steam://run/212680"], shell=True)

def main():
    parser = argparse.ArgumentParser(description='Profile saver for Faster Than Light')
    subparsers = parser.add_subparsers(title='commands', dest='command')
    
    # Define commands here
    parserHelp = subparsers.add_parser('help', help='Displays nebula ascii and manual.')
    parserHelp.set_defaults(func=help)
    
    parserSave = subparsers.add_parser('save', help='Saves the current progress to the name specified. ')
    parserSave.add_argument('name', type=str, default="NEW", help='Name of save file (default is [NEW])')
    parserSave.set_defaults(func=save)
    
    parserLoad = subparsers.add_parser('load', help='Loads the given name if such file exists, otherwise does list.')
    parserLoad.add_argument('name', type=str, default="NEW", help=
    '''
Loads the save with given name, if it doesn't exist
it lists the ones that do (same as list) and does
nothing else.
    ''')
    parserLoad.set_defaults(func=load)
    
    parserList = subparsers.add_parser('list', help='Lists the saves locally stored in specified folder. ')
    parserList.set_defaults(func=list)
    
    parserStart = subparsers.add_parser('run', help='Starts the game through steam api.')
    parserStart.set_defaults(func=run)


    args = parser.parse_args()
    if hasattr(args, 'func'):
        args.func(args)
        
    
if __name__ == '__main__':
    main()
