import * as vscode from 'vscode';

export class StatusBar {
    private static statusBarItem: vscode.StatusBarItem;
    
    constructor() {
        StatusBar.statusBarItem = vscode.window.createStatusBarItem(
            vscode.StatusBarAlignment.Right, 
            100
        );
        StatusBar.statusBarItem.show();
    }
    
    update(text: string) {
        StatusBar.statusBarItem.text = `$(comment-discussion) ${text}`;
    }
    
    static dispose() {
        StatusBar.statusBarItem.dispose();
    }
}
