import * as vscode from 'vscode';
import axios from 'axios';

const API_ENDPOINT = 'http://localhost:8000/translate';

export class Translator {
    private config = vscode.workspace.getConfiguration('accentTranslator');
    
    async translateActiveDocument(dialect: string) {
        const editor = vscode.window.activeTextEditor;
        if (!editor) return;
        
        const document = editor.document;
        const code = document.getText();
        const comments = this.extractComments(document);
        
        await editor.edit(async editBuilder => {
            for (const comment of comments) {
                try {
                    const translated = await this.translateText(
                        comment.text, 
                        dialect,
                        code
                    );
                    
                    editBuilder.replace(
                        new vscode.Range(
                            document.positionAt(comment.start),
                            document.positionAt(comment.end)
                        ),
                        translated
                    );
                } catch (error) {
                    vscode.window.showErrorMessage(
                        `Failed to translate: ${comment.text.substring(0, 30)}...`
                    );
                }
            }
        });
    }
    
    private async translateText(text: string, dialect: string, context: string): Promise<string> {
        const response = await axios.post(API_ENDPOINT, {
            comment: text,
            dialect: dialect,
            context: context
        }, {
            timeout: 5000,
            headers: {'Content-Type': 'application/json'}
        });
        
        return response.data.translated_comment;
    }
    
    private extractComments(document: vscode.TextDocument) {
        const tokenTypes = ['comment', 'string'];
        const comments = [];
        const tokens = this.getLanguageTokens(document.languageId);
        
        for (let i = 0; i < document.lineCount; i++) {
            const line = document.lineAt(i);
            if (tokens.some(token => line.text.trim().startsWith(token))) {
                comments.push({
                    text: line.text,
                    start: document.offsetAt(line.range.start),
                    end: document.offsetAt(line.range.end)
                });
            }
        }
        return comments;
    }
    
    private getLanguageTokens(languageId: string): string[] {
        const tokenMap: Record<string, string[]> = {
            'python': ['#', '"""', "'''"],
            'javascript': ['//', '/*'],
            'typescript': ['//', '/*'],
            'java': ['//', '/*'],
            'c': ['//', '/*'],
            'cpp': ['//', '/*'],
            'go': ['//', '/*']
        };
        return tokenMap[languageId] || ['//', '#', '--'];
    }
}
