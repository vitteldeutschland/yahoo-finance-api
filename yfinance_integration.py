"""
Gemini AI와의 통합을 위한 모듈
"""

from earnings_research import YahooFinanceEarningsResearch
import json

class YahooFinanceGeminiTool:
    """Gemini를 위한 Yahoo Finance 실적공시 분석 도구"""
    
    @staticmethod
    def get_earnings_report_tool():
        """실적공시 정보 조회 Tool 정의"""
        return {
            "name": "get_earnings_report",
            "description": "Yahoo Finance에서 특정 종목의 실적공시 및 최신 재무 정보를 조회합니다.",
            "parameters": {
                "type": "object",
                "properties": {
                    "ticker": {
                        "type": "string",
                        "description": "주식 종목코드 (예: AAPL, MSFT, GOOGL, TSLA 등)"
                    }
                },
                "required": ["ticker"]
            }
        }
    
    @staticmethod
    def get_quarterly_financials_tool():
        """분기별 재무제표 Tool 정의"""
        return {
            "name": "get_quarterly_financials",
            "description": "Yahoo Finance에서 분기별 재무제표 정보를 조회합니다.",
            "parameters": {
                "type": "object",
                "properties": {
                    "ticker": {
                        "type": "string",
                        "description": "주식 종목코드 (예: AAPL, MSFT, GOOGL 등)"
                    }
                },
                "required": ["ticker"]
            }
        }
    
    @staticmethod
    def get_upcoming_earnings_tool():
        """예정된 실적공시 Tool 정의"""
        return {
            "name": "get_upcoming_earnings",
            "description": "Yahoo Finance에서 예정된 실적공시 날짜 및 정보를 조회합니다.",
            "parameters": {
                "type": "object",
                "properties": {
                    "ticker": {
                        "type": "string",
                        "description": "주식 종목코드 (예: AAPL, MSFT, GOOGL 등)"
                    }
                },
                "required": ["ticker"]
            }
        }
    
    @staticmethod
    def get_financial_ratios_tool():
        """재무비율 조회 Tool 정의"""
        return {
            "name": "get_financial_ratios",
            "description": "Yahoo Finance에서 종목의 PE Ratio, ROE, Debt-to-Equity 등 주요 재무비율을 조회합니다.",
            "parameters": {
                "type": "object",
                "properties": {
                    "ticker": {
                        "type": "string",
                        "description": "주식 종목코드 (예: AAPL, MSFT, GOOGL 등)"
                    }
                },
                "required": ["ticker"]
            }
        }
    
    @staticmethod
    def get_analyst_recommendations_tool():
        """애널리스트 추천 Tool 정의"""
        return {
            "name": "get_analyst_recommendations",
            "description": "Yahoo Finance에서 애널리스트의 목표가, 추천등급 및 평가 정보를 조회합니다.",
            "parameters": {
                "type": "object",
                "properties": {
                    "ticker": {
                        "type": "string",
                        "description": "주식 종목코드 (예: AAPL, MSFT, GOOGL 등)"
                    }
                },
                "required": ["ticker"]
            }
        }
    
    @staticmethod
    def search_earnings_calendar_tool():
        """실적공시 캘린더 Tool 정의"""
        return {
            "name": "search_earnings_calendar",
            "description": "Yahoo Finance에서 향후 실적공시 일정을 조회합니다.",
            "parameters": {
                "type": "object",
                "properties": {
                    "days_ahead": {
                        "type": "integer",
                        "description": "조회할 기간 (일 단위, 기본값: 30)"
                    }
                }
            }
        }
    
    @staticmethod
    def execute_get_earnings_report(ticker: str) -> str:
        """실적공시 정보 조회 실행"""
        return YahooFinanceEarningsResearch.get_earnings_report(ticker)
    
    @staticmethod
    def execute_get_quarterly_financials(ticker: str) -> str:
        """분기별 재무제표 조회 실행"""
        return YahooFinanceEarningsResearch.get_quarterly_financials(ticker)
    
    @staticmethod
    def execute_get_upcoming_earnings(ticker: str) -> str:
        """예정된 실적공시 조회 실행"""
        return YahooFinanceEarningsResearch.get_upcoming_earnings(ticker)
    
    @staticmethod
    def execute_get_financial_ratios(ticker: str) -> str:
        """재무비율 조회 실행"""
        return YahooFinanceEarningsResearch.get_financial_ratios(ticker)
    
    @staticmethod
    def execute_get_analyst_recommendations(ticker: str) -> str:
        """애널리스트 추천 조회 실행"""
        return YahooFinanceEarningsResearch.get_analyst_recommendations(ticker)
    
    @staticmethod
    def execute_search_earnings_calendar(days_ahead: int = 30) -> str:
        """실적공시 캘린더 조회 실행"""
        return YahooFinanceEarningsResearch.search_earnings_calendar(days_ahead)
